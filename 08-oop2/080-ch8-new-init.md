

# Chapter 8.80 — `__new__()` versus `__init__()`

## What this page covers

Every earlier chapter page that used `__init__()` treated it as "the constructor" — the method that runs automatically when you create an object. That's a useful simplification for most everyday code, but it's not the whole story. This page reveals the step that actually happens *before* `__init__()`: a separate dunder method called `__new__()`, which is responsible for the physical creation of the object, before `__init__()` ever gets a chance to fill it with data.

Understanding this distinction matters for two reasons. First, it deepens your mental model of exactly what happens when you write `MyClass()` — useful for debugging unusual object-creation bugs. Second, `__new__()` unlocks a small set of genuinely useful advanced patterns — most notably the **Singleton pattern**, demonstrated on this page — that simply aren't possible using `__init__()` alone, because by the time `__init__()` runs, the object already exists and can't be swapped out for a different one.

**A few terms used throughout, explained simply, with links for more detail:**
- **Constructor** — in most everyday Python discussion, "the constructor" informally refers to `__init__()`. This page shows that, more precisely, object creation is really a *two-step* process, with `__new__()` handling creation and `__init__()` handling setup.
- **Singleton pattern** — a design pattern that restricts a class to having only ever one single object in existence, no matter how many times you try to create one. ([Wikipedia: Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern))
- **Metaclass** — a class whose instances are themselves classes (i.e., "a class of a class"). This is an advanced topic, mentioned briefly below for completeness, with a link for further reading. ([Python docs: Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses))
- **Immutable type** — a type whose value cannot be changed after creation (e.g. `str`, `tuple`, `int`). Covered further in the section below on why `__new__()` matters for these types specifically.

---

## Object creation happens in two steps

Object creation in Python is a **two-step process**, not one:

- **Step 1:** `__new__()` → creates the object
- **Step 2:** `__init__()` → initializes the object

### Simple definitions

- **`__new__()`**: creates and returns a **new object (instance)**.
- **`__init__()`**: initializes the **attributes** of an object that already exists.

---

## Comparative table

| Feature | `__new__()` | `__init__()` |
|---|---|---|
| Purpose | Creates the object | Initializes the object |
| Type | Static-like method (though technically a special case — see the note below) | Instance method |
| First parameter | `cls` (the class itself) | `self` (the specific object) |
| Called when | **Before** the object exists | **After** the object exists |
| Return value | Must return the new object | Must return `None` |
| Controls | Object *creation* | Object *customization* |
| Called first? | Yes | No |
| Can the next step be skipped? | Yes — if `__new__()` doesn't return a proper object, `__init__()` is skipped entirely | No — since `__init__()` only ever runs *after* `__new__()` has already produced an object |

*(Note on "static-like": `__new__()` is technically implemented as a `staticmethod` internally, but it's special-cased by Python to automatically receive `cls` as its first argument, unlike a normal `@staticmethod` you'd write yourself — hence "static-like" rather than a plain static method.)*

---

## Flow of execution, visualized

![Flowchart](/resources/ch-8-august-2026-new-vs-init.png)


---

## Basic demonstration

```python
class Pet:

    def __init__(self):
        # Step 2: __init__() ALWAYS runs after __new__() has already
        # successfully produced an object -- its job here is simply
        # to fill in that object's starting data.
        print("Step 2: __init__() called")
        self.name = "Default Pet"

    def __new__(cls):
        # Step 1: __new__() runs FIRST, before any object exists yet.
        # 'cls' here is the class itself (Pet), not an object.
        print("Step 1: __new__() called")

        # Crucially: we must call the PARENT class's __new__() (object's
        # own version) to actually perform the real, low-level memory
        # allocation. Overriding __new__() doesn't mean reinventing
        # object creation from scratch -- it means adding our own logic
        # AROUND the real creation step, which object still handles.
        obj = super().__new__(cls)
        return obj   # __new__() MUST return the created object.


p = Pet()
# Output:
# Step 1: __new__() called
# Step 2: __init__() called
```

### Important concept

- `__new__()` creates the object and returns it.
- That returned object is exactly what becomes `self`, the moment `__init__()` runs on it.

### Very important rule

> **If `__new__()` does not return an object, `__init__()` will not run at all.**

---

## What happens if `super().__new__(cls)` is never called

```python
class Pet:

    def __new__(cls):
        print("__new__ called")
        # The line below is intentionally commented out, to show what
        # happens when the REAL object-creation step is skipped:
        # obj = super().__new__(cls)
        # return obj
        return None   # Returning None means: "no object was created."

    def __init__(self):
        print("__init__ called")


p = Pet()
# Output:
# __new__ called
# (Notice "__init__ called" NEVER prints -- because __new__() didn't
# return a real Pet object, Python has nothing to run __init__() ON,
# so it skips that step entirely.)

print(p)
# Output: None
# 'p' is literally None here, because that's exactly what __new__()
# returned -- Python doesn't silently create a "fallback" object for
# you; whatever __new__() returns is exactly what you get back.
```

**Rule of thumb:** if you override `__new__()`, you must call `super().__new__(cls)` (or otherwise produce and return a genuine object), or object creation quietly fails to produce anything usable.

---

## Using `__new__()` to build a Singleton

This next script demonstrates one of `__new__()`'s most well-known real uses: making sure that **no matter how many times a class is "created," only one single object of it will ever actually exist.**

Normally, calling a class multiple times creates a brand-new, separate object every single time. But sometimes a design genuinely calls for only one object to exist across an entire program — a shared configuration object, a single connection to a resource, or (as here) a demonstration `SingletonPet`.

### How this script ensures only one object exists

- A class-level variable, `_instance`, stores the one object that's ever created (or `None`, if none has been created yet).
- Inside `__new__()`:
  - If `_instance` is still `None` → create a genuinely new object, and remember it.
  - If `_instance` already holds an object → simply return that *same* existing object again, instead of creating a new one.
- Because `__new__()` is what actually controls object creation, no *second* object is ever produced after the first.

**Key idea:** `__new__()` decides *whether* to create a new object at all, or simply hand back one that already exists.

```python
class SingletonPet:
    _instance = None   # Class attribute: starts empty, will later hold the ONE allowed object.

    def __new__(cls):
        if cls._instance is None:
            # Step 1: No object exists yet -- create the first (and
            # ONLY) real one, using the proper super().__new__(cls) call.
            print("Creating object")
            cls._instance = super().__new__(cls)
        else:
            # Step 2: An object already exists -- do NOT create a new
            # one. Simply fall through to returning the existing object.
            print("Using existing object")
        return cls._instance

    def __init__(self):
        # Step 3: Note that __init__() still runs EVERY time
        # SingletonPet() is called, even on the second, third, etc.
        # call -- __new__() only controls whether a NEW object is
        # made, not whether __init__() runs on whatever gets returned.
        print("Initializing object")


s1 = SingletonPet()
# Output:
# Creating object
# Initializing object

s2 = SingletonPet()
# Output:
# Using existing object
# Initializing object

print("Are both objects same?", s1 is s2)
# Output: Are both objects same? True
```

### A follow-up question worth exploring

Notice from the output above that `"Initializing object"` prints **twice** — once for `s1`, and again for `s2` — even though `s2` is really just `s1` in disguise. As a follow-up exercise: **is this a problem?** Specifically, if `__init__()` did something more consequential than printing a message — say, resetting `self.name = "New Pet"` — would that cause `s2 = SingletonPet()` to accidentally reset data that `s1` had already changed? Try adding a mutable attribute to `SingletonPet`, change it after creating `s1`, then create `s2` and check whether your change survived. (This is a well-known subtlety of implementing Singletons this way, and worth experiencing directly rather than just reading about.)

---

## The lifecycle of object creation: a closer look

1. **The two-step process:** object creation is a dual-stage sequence — first `__new__()` (allocation), then `__init__()` (initialization).
2. **Creation vs. setup:** `__new__()` is the method that creates and returns a raw, empty instance; `__init__()` is the method that populates that instance with data.
3. **Arguments:** `__new__()` receives `cls` (the class itself) as its first argument; `__init__()` receives `self` (the specific instance that `__new__()` just created).
4. **The silent ancestor:** every class automatically inherits a default `__new__()` from the base `object` class (see the earlier chapter page, "Implicit Inheritance from `object`"), which handles the actual low-level memory allocation you never normally need to think about.
5. **The return requirement:** if you override `__new__()` yourself, you **must** return a real instance — typically by calling `super().__new__(cls)`, as shown throughout this page.
6. **The dependency:** `__init__()` only runs if `__new__()` returns an instance of that specific class (or one of its subclasses) — as demonstrated in the "what happens if `super()` is never called" example above.
7. **Return types:** `__new__()` must return the instance itself; `__init__()`, by contrast, must always return `None` (Python will raise a `TypeError` if you try to make `__init__()` return anything else).
8. **The orchestrator:** classes are "callable" (i.e., you can write `MyClass()` at all) because their metaclass, `type`, implements a special `__call__` method behind the scenes.
9. **The hidden sequence:** when you write `MyClass()`, it's actually `type.__call__` that runs first, and *that* is what internally triggers the `__new__()` → `__init__()` sequence you've seen throughout this page.
10. **Immutable types:** `__new__()` is the *only* place you can customize the creation of immutable types like `tuple`, `str`, or `int`, because by the time `__init__()` would normally run, the object is already "frozen" and can't be changed — so any customization has to happen earlier, during `__new__()`.
11. **Use cases for `__new__()`:** advanced patterns like Singletons (as shown above), intercepting object creation inside metaclasses, or subclassing immutable built-in types.
12. **Use cases for `__init__()`:** the vast majority (roughly 99%) of everyday tasks — setting instance attributes and establishing an object's initial state, exactly as every earlier chapter page in this book has done.

---

## Quick recap

- Creating an object is really **two separate steps**: `__new__()` builds it, `__init__()` fills it in — most of the time you never notice this, because the default `__new__()` inherited from `object` does its job silently.
- **If `__new__()` doesn't return a proper object** (as in the `return None` example), `__init__()` is skipped entirely — this is the single most important rule to remember from this page.
- **The Singleton pattern** is the classic real-world use for overriding `__new__()`: by checking and reusing a stored `_instance`, a class can guarantee that only one object of it will ever exist — but as the follow-up question above shows, remember that `__init__()` still runs on every call, which is a subtlety worth testing for yourself.
- For the overwhelming majority of classes you'll write, **you only ever need `__init__()`** — overriding `__new__()` is a specialized tool for a small number of advanced situations (Singletons, metaclasses, immutable type customization), not something to reach for by default.


