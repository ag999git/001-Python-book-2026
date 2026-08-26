


# Chapter 8.130 — Project: Optimizing Pet Objects Using `__slots__`

## What this page covers

This page builds directly on the earlier chapter page about `__dict__`, which showed that every object normally stores its attributes in its own personal dictionary. This project explores the trade-off behind that convenience: keeping a full dictionary on every single object costs memory, and if your program creates a very large number of objects (thousands or millions of small objects, for instance), that overhead can genuinely add up. `__slots__` is Python's built-in mechanism for opting out of `__dict__` entirely, on a per-class basis, trading away some flexibility in exchange for a smaller memory footprint per object.

This is a genuinely practical, real-world optimization technique — not just a theoretical curiosity. It's commonly used in performance-sensitive code that creates huge numbers of small, simple objects (data records, graph nodes, particles in a simulation, and similar cases), where the memory saved per object, multiplied across millions of objects, becomes significant.

---

## Objective

By completing this project you will:
- Understand **why `__dict__` consumes memory**
- Learn how `__slots__` **removes `__dict__`**
- Compare the behaviour of a normal class against a class using `__slots__`
- Understand the **limitations and trade-offs** involved

---

## Task Description



You are required to:

**Step 1:** Create a normal class `PetNormal`, with `name` and `age`, stored using `self.name`, `self.age`.

**Step 2:** Create a class `PetSlots`, defining `__slots__ = ['name', 'age']`, using the same attributes as above.

**Step 3:** Create objects: `p1 = PetNormal("Tommy", 5)` and `p2 = PetSlots("Bruno", 3)`.

**Step 4:** Compare namespaces — print `p1.__dict__`, then try `p2.__dict__`. Observe and explain the difference.

**Step 5:** Add a new attribute dynamically — try `p1.color = "Brown"` and `p2.color = "Black"`. Observe which works and which fails.

**Step 6:** Compare memory (conceptually), using:
```python
import sys
print(sys.getsizeof(p1))
print(sys.getsizeof(p2))
```

**Step 7:** Write an explanation covering: what `__dict__` is, what `__slots__` does, why dynamic attributes fail on a `__slots__` class, and when to actually use `__slots__`.

### Dos and don'ts

**Do:**
- Use the same attribute names in both classes
- Print outputs clearly
- Add comments explaining the behaviour

**Don't:**
- Use different attribute names between the two classes
- Skip error handling
- Assume `__slots__` improves *speed* — the focus here is specifically **memory**, not execution speed

### Hints (very important)

- `__slots__` → **removes the instance's `__dict__`**
- Without `__dict__` → no dynamic (unplanned) attributes are possible
- Think of it as: **fixed structure vs. flexible structure**

### A follow-up question worth exploring

Step 6 compares `sys.getsizeof()` for a single `PetNormal` object against a single `PetSlots` object — and the actual difference for just one object is often smaller than you might expect (see the note on this in the script below). As a follow-up exercise: **create 100,000 objects of each class in a loop, and compare the *total* memory difference** (you can use `sys.getsizeof()` summed across all objects, or a library like `tracemalloc` for a more accurate picture). This should make the real-world benefit of `__slots__` far more visible than comparing just one object of each type ever could.

---

## Expected observations

| Feature | `PetNormal` | `PetSlots` |
|---|---|---|
| Has `__dict__`? | Yes | No |
| Dynamic attributes allowed? | Yes | No |
| Memory usage (at scale) | Higher | Lower |
| Flexibility | High | Low |


![Flowchart](/resources/ch-8-august-2026-pet-slots-project.png)

---

## The script

```python
# ============================================================
# STEP 1: A NORMAL CLASS -- keeps the default __dict__
# ============================================================
class PetNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ============================================================
# STEP 2: A CLASS USING __slots__ -- opts out of __dict__
# ============================================================
class PetSlots:
    # Declaring __slots__ tells Python: "instances of this class will
    # ONLY ever have these named attributes -- nothing else." Because
    # of this promise, Python doesn't need to give each instance a
    # full __dict__ at all; it can store 'name' and 'age' in a more
    # compact, fixed-size internal structure instead.
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


# ============================================================
# STEP 3: OBJECT CREATION
# ============================================================
p1 = PetNormal("Tommy", 5)
p2 = PetSlots("Bruno", 3)


# ============================================================
# STEP 4: NAMESPACE COMPARISON
# ============================================================
print("PetNormal __dict__:", p1.__dict__)
# Output: PetNormal __dict__: {'name': 'Tommy', 'age': 5}
# PetNormal has no __slots__, so it keeps the default, fully dynamic
# __dict__ that every ordinary object gets (see the earlier chapter
# page on __dict__ for the full explanation of this).

try:
    print("PetSlots __dict__:", p2.__dict__)
except AttributeError as e:
    print("PetSlots has no __dict__:", e)
# Output: PetSlots has no __dict__: 'PetSlots' object has no attribute '__dict__'
# This is the entire point of __slots__: PetSlots objects are built
# WITHOUT a __dict__ at all -- there's nothing there to print.


# ============================================================
# STEP 5: DYNAMIC ATTRIBUTE ADDITION
# ============================================================

# This WORKS, because PetNormal still has a __dict__ -- adding a new
# key, "color", is exactly the same operation as adding a new key to
# any other dictionary.
p1.color = "Brown"
print("PetNormal new attribute:", p1.color)   # -> PetNormal new attribute: Brown

# This FAILS, because PetSlots has no __dict__ to add a new key to --
# Python has nowhere to physically store an attribute that wasn't
# declared in __slots__ ahead of time.
try:
    p2.color = "Black"
except AttributeError as e:
    print("Cannot add new attribute to PetSlots:", e)
# Output: Cannot add new attribute to PetSlots: 'PetSlots' object has
# no attribute 'color'


# ============================================================
# STEP 6: MEMORY COMPARISON
# ============================================================
import sys

print("Memory (PetNormal):", sys.getsizeof(p1))
print("Memory (PetSlots):", sys.getsizeof(p2))
# A note on interpreting this output: sys.getsizeof() only measures
# the size of the OBJECT ITSELF -- for PetNormal, this does NOT
# automatically include the separate __dict__ object it points to
# (you'd need to add sys.getsizeof(p1.__dict__) to get the full
# picture). Because of this, the difference between a SINGLE
# PetNormal and a SINGLE PetSlots object can look smaller than you'd
# expect from this comparison alone. The real savings from __slots__
# become obvious at SCALE -- see the follow-up question above for an
# exercise that makes this much more visible.
```

---

## Explanation (Step 7)

**What is `__dict__`?** As covered on the earlier chapter page, `__dict__` is the actual dictionary Python uses to store an object's own attributes — every ordinary object gets one automatically, and it's what makes adding new attributes to an object at any time ("dynamic attributes") possible.

**What does `__slots__` do?** Declaring `__slots__` inside a class body tells Python exactly which attribute names instances of this class are allowed to have, ahead of time. In exchange for that restriction, Python stops giving instances a `__dict__` at all, storing the declared attributes in a smaller, fixed-size structure instead.

**Why do dynamic attributes fail on a `__slots__` class?** Without a `__dict__`, there's simply no flexible container left to add a new key to — Python has no mechanism to attach an attribute that wasn't explicitly declared in `__slots__`, so it raises an `AttributeError` instead.

**When should you actually use `__slots__`?** When you're creating a **very large number** of instances of a simple class with a small, fixed, well-known set of attributes, and per-object memory usage genuinely matters for your program. It's not a general-purpose optimization for every class — for the vast majority of everyday code, the flexibility of a normal `__dict__`-based class is worth far more than the memory it costs.

---

## Quick recap

- **Every ordinary Python object stores its own attributes in a `__dict__`**, which gives it the flexibility to gain new attributes at any time — but that flexibility isn't free; the dictionary itself takes up memory.
- **`__slots__` trades that flexibility for a smaller memory footprint**, by declaring a fixed, known set of attribute names up front and removing `__dict__` entirely.
- **The cost is real: no dynamic attributes at all** — anything not explicitly listed in `__slots__` will raise an `AttributeError` the moment you try to assign it.
- **The benefit only becomes meaningful at scale** — comparing `sys.getsizeof()` for a single object of each kind understates the real difference, since `__dict__`'s own memory cost isn't included in that measurement; the follow-up exercise above (creating 100,000 objects of each kind) shows the real-world impact far more clearly.
- **`__slots__` is a specialized tool for memory-sensitive, large-scale object creation** — not a general-purpose habit to apply to every class you write.





