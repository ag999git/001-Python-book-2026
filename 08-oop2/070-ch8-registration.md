
# Chapter 8.70 — Research Project: Three Ways to Build a Pet Registration System

## What this page covers

This page is a research/project assignment for Chapter 8 that steps a little outside pure inheritance and into a genuinely practical design pattern: the **class registry**. A registry is simply a place — usually a dictionary — that keeps track of which classes exist in a system, so that new objects can be created dynamically by *name*, rather than needing to be hardcoded with `if/elif` chains every time you add a new type. This page compares three different ways of building such a registry in Python, each trading off simplicity against automation.

This is a genuinely useful, real-world pattern — it's how many frameworks and plugin systems let you "register" new components (new pet types here, but the same idea applies to new game characters, new payment methods, new file format handlers, and so on) without the core system needing to know about every specific type in advance.

**A few terms used throughout, explained simply, with links for more detail:**
- **Class registry pattern** — a design pattern where classes are stored in a lookup structure (often a dictionary) so they can be found and used by name at runtime. ([Wikipedia: Registry pattern](https://en.wikipedia.org/wiki/Service_locator_pattern))
- **`@classmethod`** — a method that receives the *class itself* (conventionally named `cls`) as its first argument, rather than a specific object (`self`). This is what lets `PetRegistryManual.register(...)` be called directly on the class, without ever creating a `PetRegistryManual` object. ([Python docs: `classmethod`](https://docs.python.org/3/library/functions.html#classmethod))
- **Closure** — a function defined inside another function, which "remembers" variables from the outer function even after the outer function has finished running. This is what makes the decorator-based approach below work (covered in more depth on the earlier chapter page, "Using `functools.wraps` in Decorators").
- **`__init_subclass__`** — a special hook method that Python calls automatically every time a new subclass of a class is defined — not when an *object* is created, but the moment the *class itself* is defined. ([Python docs: `__init_subclass__`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__))

---

## Research / Project Question: Design a Pet Registration System Using 3 Approaches



You are required to design a **Pet Management System** that demonstrates three different ways of registering classes in Python.

### Requirements

**Part A: Manual Registration**
1. Create a class `PetRegistryManual`
2. Maintain a dictionary `registry`
3. Provide a method `register(name, cls)`
4. Create classes: `Dog`, `Cat`
5. Manually register them
6. Dynamically create objects and call `speak()`

**Part B: Decorator-Based Registration**
1. Create a class `PetRegistryDecorator`
2. Implement a decorator method `register(name)`
3. Register classes using `@decorator`
4. Create: `Bird`, `Fish`
5. Dynamically call their methods

**Part C: Automatic Registration (`__init_subclass__`)**
1. Create base class `Pet`
2. Automatically register subclasses using `__init_subclass__()`
3. Create: `Horse`, `Cow`
4. Print all registered subclasses
5. Dynamically create objects

**Final Task:** Compare all 3 approaches. State advantages and disadvantages.

### A follow-up question worth exploring

All three approaches shown below only ever *add* classes to the registry — none of them ever needs to *remove* one. As a natural extension: **how would you add an `unregister(name)` capability to each of the three approaches?** For manual and decorator registration this is fairly direct (just `del registry[name]`), but for the automatic `__init_subclass__` approach it's more subtle — a class, once defined, can't easily "un-define" itself. This asymmetry is itself a useful design insight, worth thinking through even without writing the code.

---

## Core idea

All three approaches aim to achieve the exact same underlying goal:

> **Store class references so they can be looked up and used dynamically, by name, rather than being hardcoded.**

They differ only in *when* and *how* that storing happens.

| Approach | Idea | Why it's used |
|---|---|---|
| **1. Manual Registration** | The programmer explicitly registers each class with a separate line of code | Simple and easy to understand — a good starting point for beginners |
| **2. Decorator Registration** | Registration happens automatically, right at the moment each class is *defined*, via `@decorator` syntax | Cleaner and safer than manual registration — much harder to forget |
| **3. Automatic Registration** | The base class itself automatically tracks every subclass that's ever created, with no extra code needed on each subclass | Best for large systems and frameworks, where you can't rely on every contributor remembering to register their own classes |

```mermaid
graph TD
    Goal[Goal - look up classes by name at runtime]
    Manual[Approach 1 - Manual - explicit register call]
    Decorator[Approach 2 - Decorator - automatic at definition]
    Auto[Approach 3 - init_subclass - fully automatic]

    Goal --> Manual
    Goal --> Decorator
    Goal --> Auto
```




## Approach 1: Manual Registration

**Idea:** The programmer explicitly calls a `register()` function for every class, as a separate step after defining it.

```python
# --- A. The registry itself ---
class PetRegistryManual:
    # Step 1: A class attribute -- one single dictionary, SHARED by
    # the whole class (not one copy per object), used to store
    # {name: class} pairs.
    registry = {}

    @classmethod
    def register(cls, name, pet_class):
        # Step 2: A classmethod, so this can be called directly on
        # the class itself -- PetRegistryManual.register(...) --
        # without ever needing to create a PetRegistryManual object.
        cls.registry[name] = pet_class


# --- B. Pet classes, defined completely independently of the registry ---
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")


# --- C. Manual registration -- a SEPARATE step, easy to forget ---
PetRegistryManual.register("dog", Dog)
PetRegistryManual.register("cat", Cat)

# --- D. Dynamic usage: look up a class by NAME, not by writing it directly ---
PetClass = PetRegistryManual.registry["dog"]   # PetClass now refers to the Dog class itself
pet = PetClass()                                # Create a Dog object via that reference
pet.speak()                                     # -> Dog barks

PetClass = PetRegistryManual.registry["cat"]
pet = PetClass()
pet.speak()                                     # -> Cat meows
```

**The main risk with this approach:** nothing forces you to remember the registration step. If you define a new `Rabbit` class but forget to call `PetRegistryManual.register("rabbit", Rabbit)`, your program won't error immediately — `"rabbit"` simply won't be usable through the registry, and the bug might not surface until much later.

---

## Approach 2: Decorator-Based Registration

**Idea:** Registration happens automatically, the instant a class is *defined*, by attaching `@PetRegistryDecorator.register("name")` directly above the class definition.

```python
class PetRegistryDecorator:
    registry = {}

    @classmethod
    def register(cls, name):
        # Step 1: This OUTER function's job is just to "remember" the
        # name (e.g. "bird") and hand back a second, INNER function.
        def wrapper(pet_class):
            # Step 2: This INNER function is a CLOSURE -- it still has
            # access to 'name' and 'cls' from the outer function, even
            # though the outer function has already finished running
            # by the time this actually executes.
            cls.registry[name] = pet_class
            return pet_class   # Must return the class unchanged, so
                                # the name "Bird" still refers to the
                                # real Bird class after the decorator runs.
        return wrapper


# --- Registration happens IMMEDIATELY, as each class is defined ---
@PetRegistryDecorator.register("bird")
class Bird:
    def speak(self):
        print("Bird chirps")

@PetRegistryDecorator.register("fish")
class Fish:
    def speak(self):
        print("Fish bubbles")

# --- Dynamic usage, exactly the same pattern as Approach 1 ---
PetClass = PetRegistryDecorator.registry["bird"]
pet = PetClass()
pet.speak()   # -> Bird chirps

PetClass = PetRegistryDecorator.registry["fish"]
pet = PetClass()
pet.speak()   # -> Fish bubbles
```

**Why this is safer than Approach 1:** the registration call and the class definition are now physically stuck together — it's much harder to define a class and forget to register it, because the decorator line sits directly above the `class` keyword, impossible to miss during a code review.

---

## Approach 3: Automatic Registration (`__init_subclass__`)

**Idea:** Rather than registering each class individually (by hand, or via a decorator), the *base class itself* automatically registers every subclass the moment it's defined — no extra code needed on `Horse`, `Cow`, or any future subclass at all.

```python
class Pet:
    # Step 1: A single list, shared by the whole Pet class hierarchy,
    # that will automatically fill up with every subclass ever defined.
    registry = []

    def __init_subclass__(cls):
        # Step 2: Python calls this AUTOMATICALLY, every single time a
        # new subclass of Pet is defined -- not when an object is
        # created, but at the moment the CLASS ITSELF is defined.
        # 'cls' here is the new subclass (e.g. Horse, the first time
        # this runs for Horse).
        super().__init_subclass__()
        # Step 3: Register the new subclass automatically -- no
        # separate register() call needed anywhere else in the code.
        Pet.registry.append(cls)


# --- Simply inheriting from Pet is enough -- registration is automatic ---
class Horse(Pet):
    def speak(self):
        print("Horse neighs")

class Cow(Pet):
    def speak(self):
        print("Cow moos")

# --- Dynamic usage: loop through EVERY registered subclass at once ---
for cls in Pet.registry:
    obj = cls()
    obj.speak()
# Output:
# Horse neighs
# Cow moos
# Notice: at no point did we write "Pet.registry.append(Horse)" or
# anything similar -- simply writing "class Horse(Pet):" was enough
# to trigger registration automatically.
```

**Why this is the strongest guarantee of the three:** it's structurally impossible to forget to register a subclass, because registration isn't a separate step at all — it's baked directly into what "being a subclass of `Pet`" *means*. This is exactly the kind of guarantee large frameworks rely on, where many different contributors might be adding new subclasses without ever needing to know a registry exists at all.

---

## Comparison table

| Feature | Manual | Decorator | Automatic (`__init_subclass__`) |
|---|---|---|---|
| Registration | Explicit — a separate call you must remember | Automatic, tied directly to class definition | Fully automatic — inheriting is enough |
| Ease of understanding | Easy | Medium | Medium |
| Flexibility | Low | High | Medium |
| Risk of forgetting | High | Low | Very low |
| Best use case | Small scripts | Applications | Frameworks and plugin systems |

---

## Quick recap

- All three approaches solve the same problem — **looking up a class by name at runtime** — and differ only in *how automatically* that lookup gets populated.
- **Manual registration** is the simplest to understand, but the easiest to forget — nothing stops a class from silently existing outside the registry.
- **Decorator registration** ties the registration call directly to the class definition, using a `@classmethod` combined with a closure, making the connection between "defining a class" and "registering it" visually obvious and hard to skip.
- **`__init_subclass__` registration** removes the need for any registration step at all — simply inheriting from the base class is enough, which makes it the safest option for large systems where you can't rely on every contributor remembering an extra step.
- The right choice, as with the earlier Has-A relationship pages, depends on the scale and context of what you're building — a small script may not need more than manual registration, while a plugin-based framework benefits enormously from the automatic approach.





