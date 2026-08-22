
# Chapter 7 — Research Question: Shallow Copy vs. Deep Copy

## What this page covers

This page continues the Chapter 7 research series on how Python actually manages objects in memory. The earlier pages showed that a variable name is just a *label* pointing to an object on the Heap, and that assignment (`p2 = p1`) creates a second label for the **same** object rather than a new copy. This page tackles the natural follow-up question: **if I actually want an independent copy, how do I get one — and what does "independent" even mean when an object contains other objects?**

This is directly relevant any time you work with **nested data** — a list of custom objects, a dictionary of lists, an object that stores another object as an attribute, and so on — which is extremely common in real Python programs. Copying such structures carelessly is a classic source of bugs: you change what you think is your own private copy, and the original data changes too, seemingly by magic. Understanding shallow vs. deep copy removes that magic.

By the end of this page you should be able to:
- Explain the difference between copying a *container* and copying the *objects inside it*.
- Predict whether a change made through one copy will "leak" into another, for both shallow and deep copies.
- Choose the right kind of copy for a given situation, based on performance and independence trade-offs.

---

## Research Question 2: Compare and contrast shallow copy and deep copy

> When should a programmer use one over the other when working with nested objects (like a list of `Pet` objects)?

### Answer

Python's `copy` module provides two different ways to duplicate data, and the difference between them only becomes visible once your data is **nested** — for example, a list that contains objects, rather than a list of plain numbers or strings.

1. **Shallow copy (`copy.copy()`)** creates a **new container** (e.g. a new list), but fills that new container with **references to the very same inner objects** as the original. The outer box is new; everything inside it is still shared.
2. **Deep copy (`copy.deepcopy()`)** creates a new container **and** recursively creates brand-new copies of every object found inside it (and inside *those*, and so on). The result is a fully independent clone, top to bottom.

| Feature | Shallow copy | Deep copy |
|---|---|---|
| Creates a new container? | Yes | Yes |
| Creates new inner objects? | No — inner objects are **shared** with the original | Yes — inner objects are **independently cloned** |
| Changing a shared inner object | Visible in **both** the original and the copy | Visible **only** in the copy that was changed |
| Performance | Fast, low memory | Slower, uses more memory (especially for deeply nested data) |
| Good default when... | The inner objects are simple/immutable, or you *want* them shared | The inner objects are mutable and must be fully independent |

### Visualizing the difference

```mermaid
flowchart TB
    subgraph Original["original_shelter list"]
        O["original_shelter[0]"]
    end
    subgraph Shallow["shallow_shelter list (new list object)"]
        S["shallow_shelter[0]"]
    end
    subgraph Deep["deep_shelter list (new list object)"]
        D["deep_shelter[0]"]
    end
    TigerShared["Tiger object\n(name = 'Tiger')"]
    TigerClone["Tiger CLONE\n(name = 'Tiger')"]

    O --> TigerShared
    S -.->|same reference| TigerShared
    D --> TigerClone
```

Notice that `original_shelter[0]` and `shallow_shelter[0]` both point at the **same** `Tiger` object — that's what "shallow" means here. `deep_shelter[0]`, on the other hand, points at a completely separate `Tiger` clone, with its own independent memory address.

---

## The script, with explanatory comments

```python
import copy   # copy.copy() for shallow copies, copy.deepcopy() for deep copies

class Pet:
    def __init__(self, name):
        self.name = name

# 1. Create the original list, containing one Pet object
dog = Pet("Tiger")
original_shelter = [dog]

# 2. Perform a shallow copy
# copy.copy() builds a NEW list object, but each SLOT in that new list
# still points to the exact same Pet object(s) as the original list.
shallow_shelter = copy.copy(original_shelter)

# 3. Perform a deep copy
# copy.deepcopy() builds a NEW list, AND walks inside it, creating a
# brand-new, independent Pet object for every Pet it finds.
deep_shelter = copy.deepcopy(original_shelter)

print(f"Original Name: {dog.name}")
print("-" * 30)

# 4. THE TEST: change the original dog's name
print("ACTION: Changing Tiger's name to 'Sheru' in the original list...")
dog.name = "Sheru"
# This only changes the Pet object itself. It does NOT touch either
# copied list -- but it DOES affect anything still pointing at that
# same Pet object, which is exactly what the next two prints reveal.

# 5. Check the results
print(f"Shallow Copy result: {shallow_shelter[0].name} (Points to same memory)")
# -> "Sheru": the shallow copy's Pet IS dog, so the rename is visible here too.

print(f"Deep Copy result:    {deep_shelter[0].name} (Is a separate object)")
# -> "Tiger": the deep copy's Pet is a totally separate clone, made
#    BEFORE the rename, so it never sees the change.

# PROOF using id() -- comparing memory addresses confirms the story above
print(f"\nOriginal ID: {id(original_shelter[0])}")
print(f"Shallow ID:  {id(shallow_shelter[0])} -> Identical to Original")
print(f"Deep ID:     {id(deep_shelter[0])} -> Different from Original")
```

### Expected output

```text
Original Name: Tiger
------------------------------
ACTION: Changing Tiger's name to 'Sheru' in the original list...
Shallow Copy result: Sheru (Points to same memory)
Deep Copy result:    Tiger (Is a separate object)

Original ID: 140312831234576
Shallow ID:  140312831234576 -> Identical to Original
Deep ID:     140312831239120 -> Different from Original
```

The `id()` values are the real proof: `original_shelter[0]` and `shallow_shelter[0]` share the exact same address, while `deep_shelter[0]` has a completely different one — confirming it's a genuinely separate object in memory.

---

## Why does this happen? (The list vs. its contents)

It helps to remember that a Python list doesn't *contain* objects directly — it contains **references** to objects, just like a variable name does. `copy.copy()` only duplicates the list's own references; it never looks at what those references point to. `copy.deepcopy()` goes one step further: for every reference it copies, it also makes a fresh copy of the object on the *other end* of that reference, and repeats the process for anything nested inside those objects too — which is why it's called "deep."

| Copy type | What gets duplicated |
|---|---|
| Shallow copy | Just the outer container (the list itself) |
| Deep copy | The outer container, **and** every object reachable from inside it, at every nesting level |

---

## When should you use which?

```mermaid
flowchart TD
    A["Do you need to modify the\ninner objects independently?"] -->|No, read-only or immutable data| B["Use shallow copy\n(copy.copy) -- faster, less memory"]
    A -->|Yes, inner objects will be\nmodified separately| C["Use deep copy\n(copy.deepcopy) -- safe, independent"]
```

- **Choose a shallow copy** when the inner objects are immutable (like numbers or strings), or when you specifically *want* the copy and original to stay linked — for example, two different "views" over the same underlying data that should always agree.
- **Choose a deep copy** whenever you're duplicating a structure of **mutable** objects (like a list of `Pet` objects) and you need the copy to be a truly independent snapshot — for example, saving a backup of a game state before letting the player make changes, where the backup must never be affected by what happens next.
- **Watch the cost:** deep copies take more time and memory, especially for large or deeply nested structures, since every object at every level gets recursively cloned. For simple, small structures the difference is negligible; for large object graphs, it's worth being deliberate about which one you actually need.

---

## Quick recap

- Both `copy.copy()` and `copy.deepcopy()` create a new *container* — the difference is entirely about what happens to the objects **inside** it.
- A shallow copy shares its inner objects with the original; changing a shared inner object through one list changes it "everywhere," because there's really only one object.
- A deep copy recursively clones every inner object, producing a fully independent structure that no longer reacts to changes made elsewhere.
- When in doubt with nested, mutable data (like a list of custom objects) that you plan to modify independently, `copy.deepcopy()` is the safer default — just be mindful of the extra time and memory it costs on large structures.
