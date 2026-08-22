# Chapter 7.9 — Research Question: What Is a Memory Leak in Python?

## What this page covers

This page closes out the Chapter 7 research series on Python's memory model. The earlier pages established how objects live on the Heap, how `del`/`__del__()` and reference counting work, how circular references can defeat reference counting, and how `gc.collect()` acts as a backup. This page ties all of that together to answer a question beginners often assume doesn't apply to Python at all: **can a Python program actually run out of memory, even though Python cleans up after itself automatically?**

The short answer is yes — and understanding *how* is genuinely useful, not just theoretical. Long-running programs (web servers, background workers, data pipelines, GUI apps) are exactly where memory leaks quietly build up over hours or days, eventually causing crashes or major slowdowns. Knowing the common patterns that cause leaks in Python will help you spot them in your own code before they become a production problem.

By the end of this page you should be able to:
- Define what a memory leak is, precisely, in Python's context.
- Explain the two main ways a leak can happen even with automatic garbage collection.
- Recognise a classic "forgotten reference" leak in code, and know how to avoid it.

---

## Research Question 3: What is a memory leak, and how can it still happen in Python?

> Define a **Memory Leak** in the context of a Python application. Since Python has an automatic Garbage Collector, how is it still possible for a memory leak to occur?

### Answer

A **memory leak** happens when a program keeps holding on to memory it no longer actually needs. Crucially, this isn't about Python's Garbage Collector being broken or unreliable — it's about the Garbage Collector doing exactly what it's designed to do: **it only ever frees memory that has become unreachable.** If your own code is still holding a reference to something — even by accident — the Garbage Collector has no way of knowing you're "done" with it, and correctly leaves it alone. A leak, then, is really a bug in *your* code's bookkeeping, not a failure of Python's memory management.

| Cause | What happens | Why the Garbage Collector doesn't help |
|---|---|---|
| **Forgotten references** | Objects keep getting added to a long-lived structure — a global list, a dictionary, a cache — and are never removed | The objects are genuinely still reachable (via that list/dict), so they're not garbage at all — they're just unwanted |
| **Complex circular references** | Certain object graphs — especially ones with custom `__del__()` methods, or reference cycles spread across C extensions — can confuse or slow down the generational collector | The collector may need extra passes to untangle them, or (in older Python versions, pre-3.4) may refuse to collect cycles involving `__del__()` at all |
| **The result, either way** | Your program's RAM usage keeps climbing over time | Eventually the OS runs out of memory to give the process, and it slows to a crawl or crashes |

```mermaid
flowchart LR
    A[Program starts] --> B[Objects are created<br/>during normal operation]
    B --> C{Are all references<br/>to old objects removed<br/>when no longer needed?}
    C -->|Yes| D[Objects become unreachable<br/>Garbage Collector frees them]
    D --> B
    C -->|No - still referenced<br/>somewhere, e.g. a growing list| E[Objects stay alive forever<br/>RAM usage keeps climbing]
    E --> F[Eventually: slowdown or<br/>out-of-memory crash]
```

---

## A classic example: the "forgotten reference" leak

The most common real-world Python memory leak looks nothing like a bug at first glance — it's usually a list or dictionary that's meant to be a temporary cache, but nothing ever removes old entries from it.

```python
# This script demonstrates the single most common cause of memory
# leaks in real Python programs: a long-lived container (here, a
# global list) that keeps growing because nothing ever removes
# old entries from it.

class Pet:
    def __init__(self, name):
        self.name = name
        # In a real program, imagine this object also held a large
        # amount of data -- an image, a database connection, etc.


# This list is meant to be a short-term "cache" of recently seen
# pets, but notice: nothing in this script ever removes anything
# from it.
_pet_cache = []

def process_pet(name):
    """Simulates handling a Pet object and (accidentally) keeping
    a permanent reference to it in the module-level cache."""
    pet = Pet(name)
    print(f"Processing {pet.name}...")

    # THE LEAK: every call appends to _pet_cache and never removes
    # anything. As long as _pet_cache exists, every Pet object ever
    # created here stays reachable -- so the Garbage Collector will
    # correctly refuse to free any of them, forever.
    _pet_cache.append(pet)


# Simulate a long-running program processing many pets over time.
for i in range(5):
    process_pet(f"Pet-{i}")

print(f"\nCache now holds {len(_pet_cache)} Pet objects.")
# In a real long-running service, this loop might run for days,
# with _pet_cache silently growing the whole time.
```

### The fix

The fix is almost never a Garbage Collector trick — it's simply making sure your own code removes references it no longer needs:

```python
# Option 1: Explicitly trim the cache once it grows past a limit.
MAX_CACHE_SIZE = 100

def process_pet_bounded(name):
    pet = Pet(name)
    _pet_cache.append(pet)
    if len(_pet_cache) > MAX_CACHE_SIZE:
        _pet_cache.pop(0)   # remove the oldest entry, keeping the cache bounded


# Option 2: Use a weak reference so the cache doesn't keep objects
# alive by itself -- once nothing ELSE references a Pet, it can
# still be garbage collected even while "in" the cache.
import weakref
_pet_weak_cache = weakref.WeakValueDictionary()

def process_pet_weak(name):
    pet = Pet(name)
    _pet_weak_cache[name] = pet   # does not, by itself, keep pet alive
    return pet
```

| Approach | How it prevents the leak |
|---|---|
| Bounded cache (Option 1) | Old entries are explicitly removed once a size limit is reached, so the list can never grow forever |
| `weakref` (Option 2) | The cache holds a *weak* reference, which the Garbage Collector is allowed to ignore — so objects can still be freed even while technically "in" the cache |

---

## Why this matters more in long-running programs

A short script that runs for a second and exits will never notice a leak like this — it doesn't live long enough for the cache to matter. The problem shows up in exactly the kind of programs Python is heavily used for: web servers, background task workers, chat bots, data pipelines, and GUI applications, all of which are designed to keep running for hours, days, or weeks. In those contexts, even a "small" leak — a few kilobytes added per request — can add up to gigabytes over time, which is why understanding this pattern matters even though Python's memory management is automatic.

---

## Quick recap

- A memory leak in Python isn't a failure of the Garbage Collector — it's memory that's technically still *reachable* by your own code, even though your program doesn't actually need it anymore.
- **Forgotten references** (a cache, list, or dictionary that only ever grows) are by far the most common real-world cause.
- **Complex circular references**, especially involving custom `__del__()` methods, can also slow down or complicate cleanup, even though Python's generational collector is designed to eventually catch ordinary cycles.
- The fix is almost always in your own code: bound the size of long-lived containers, remove entries you no longer need, or use `weakref` when you want to track objects without keeping them alive.

