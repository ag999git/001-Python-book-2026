

# Chapter 8.91 — Metaclasses, Part 2: Practical Use Cases

## What this page covers

The previous chapter page introduced metaclasses conceptually: `type` is the built-in metaclass that quietly creates every class you write, and you can build a *custom* metaclass by inheriting from `type` yourself. This page turns that theory into three practical, genuinely useful patterns: **enforcing rules on classes**, **automatically registering classes**, and **automatically adding attributes to classes** — all without any individual subclass needing to opt in or remember an extra step.

These three patterns are exactly the kind of "magic" you'll encounter in real-world frameworks (Django's models, various plugin systems, and testing frameworks all lean on custom metaclasses somewhere under the hood). Seeing simplified versions built from scratch here should make that "magic" feel a lot less mysterious the next time you encounter it in a library you're using.

*(This page assumes you've read the previous page, "Metaclasses, Part 1: Basic Concepts," which explains what a metaclass is and how `type(name, bases, dictionary)` works — both are used directly below.)*

---

## Use Case 1: Enforce Rules on Classes

**The idea:** a metaclass can inspect a class **the moment it's being created**, and refuse to let it exist at all if it doesn't follow a required rule — here, that every `Pet` subclass must implement a `speak()` method.

This is a stronger guarantee than the Abstract Base Class approach from earlier in this chapter: an ABC stops you from *creating an object* of an incomplete class, but the incomplete *class itself* still exists. A metaclass like the one below can refuse to let the incomplete *class* exist in the first place — the error happens even earlier, right when Python processes the `class Cat:` line.

```python
# A metaclass is a class OF a class -- it defines how a class itself
# gets built. Every class is an "instance" of some metaclass (usually
# type, unless you specify a custom one, as we do here).

# Step 1: Define a custom metaclass by inheriting from 'type' -- this
# is what makes PetMeta a metaclass, rather than an ordinary class.
class PetMeta(type):
    def __new__(mcs, name, bases, dct):
        # Step 2: 'dct' is the dictionary of everything defined inside
        # the class body (methods, attributes) -- so checking whether
        # "speak" is a KEY in this dictionary tells us whether the
        # class actually defined a speak() method itself.
        if "speak" not in dct:
            raise TypeError(f"{name} must implement speak()")
        # Step 3: If the check passes, hand off to type's own __new__
        # to actually build the class, exactly as normal.
        return super().__new__(mcs, name, bases, dct)


# Step 4: Dog implements speak(), so class creation succeeds normally.
class Dog(metaclass=PetMeta):
    def speak(self):
        print("Bark")


# Step 5: Cat does NOT implement speak() -- this line will raise a
# TypeError the MOMENT Python tries to create the Cat class, before
# any Cat object could ever be created.
class Cat(metaclass=PetMeta):
    pass
# Output: TypeError: Cat must implement speak()
```

![Flowchart](/resources/ch-8-august-2026-using-metaclasses-advanced.png)


---

## Use Case 2: Automatic Registration

**The idea:** combine the enforcement pattern above with the automatic-registration idea from the earlier chapter page (which used `__init_subclass__`). A metaclass can do the exact same job — automatically tracking every subclass — but at an even earlier point in the process (class creation itself, rather than a subclass hook).

This pattern is genuinely used in plugin systems, frameworks, and tools like Django's model system, where new components need to become known to the overall system automatically, the instant they're defined.

```python
# Step 1: A global registry list, shared across the whole program,
# that will automatically fill up with every registered Pet subclass.
registry = []

class PetMeta(type):
    def __new__(mcs, name, bases, dct):
        # Step 2: Build the class first, exactly as normal.
        cls = super().__new__(mcs, name, bases, dct)
        # Step 3: Register it -- UNLESS this is the base class itself
        # (Pet), since we only want actual pet TYPES in the registry,
        # not the generic base class they all inherit from.
        if name != "Pet":
            registry.append(cls)
        return cls


# Step 4: Pet is the base class. It intentionally does NOT implement
# speak() -- and that's fine here, because THIS version of PetMeta
# doesn't enforce that rule (unlike Use Case 1's PetMeta above).
class Pet(metaclass=PetMeta):
    pass

# Step 5: Dog and Cat both inherit PetMeta automatically, simply by
# inheriting from Pet -- neither needs to write "metaclass=PetMeta"
# again themselves.
class Dog(Pet):
    def speak(self):
        print("Dog barks")

class Cat(Pet):
    def speak(self):
        print("Cat meows")

print(registry)
# Output: [<class '__main__.Dog'>, <class '__main__.Cat'>]

# Step 6: Dynamically create and use every registered class, without
# ever hardcoding "Dog" or "Cat" by name in this loop.
for cls in registry:
    obj = cls()
    obj.speak()
# Output:
# Dog barks
# Cat meows
```

**Why this matters:** notice that at no point did anyone write `registry.append(Dog)` or `registry.append(Cat)` — simply *inheriting from `Pet`* was enough to trigger registration automatically, because every subclass creation passes through `PetMeta.__new__`.

---

## Use Case 3: Automatically Add Methods/Attributes

**The idea:** a metaclass can reach directly into a class's dictionary (`dct`) *before* the class is even finished being built, and inject its own attributes — giving every class built with this metaclass some shared feature, without any individual class needing to define it.

```python
class PetMeta(type):
    def __new__(mcs, name, bases, dct):
        # Step 1: mcs is the metaclass itself (PetMeta); name is the
        # new class's name (a string); bases is a tuple of parent
        # classes; dct is the dictionary of everything defined inside
        # the class body so far.

        # Step 2: Inject a brand-new attribute directly into the
        # dictionary, BEFORE the class is actually built. Every class
        # that uses PetMeta will automatically end up with this,
        # whether or not it explicitly defines "category" itself.
        dct["category"] = "Animal"

        return super().__new__(mcs, name, bases, dct)


class Dog(metaclass=PetMeta):
    def speak(self):
        print("Bark")


dog = Dog()

print("Dog category:", Dog.category)         # -> Dog category: Animal
print("Dog category via instance:", dog.category)   # -> Dog category via instance: Animal
# Both the CLASS (Dog.category) and any INSTANCE of it (dog.category)
# can access "category" -- because it was added at the class level,
# it's automatically visible through every object of that class too,
# exactly like any other class attribute (see the earlier chapter
# page on class variables vs. instance variables).
```

### What if a class doesn't define `speak()`?

This particular `PetMeta` only adds the `category` attribute — it doesn't check for a `speak()` method at all, so a class is free to skip defining `speak()` entirely:

```python
class Cat(metaclass=PetMeta):
    pass

print(Cat.category)   # -> Animal (added automatically, same as Dog)

cat = Cat()
# cat.speak()   # This would raise an AttributeError if called, simply
                 # because speak() was never defined anywhere on Cat.
```

*(If you want a single metaclass that both enforces `speak()` **and** auto-adds `category`, you can combine both checks inside one `__new__()` method — see the follow-up question below.)*

---

## Comparing the three use cases

| Use Case | What the metaclass does | Real-world analogy |
|---|---|---|
| 1. Enforce Rules | Refuses to create a class that breaks a required rule | Similar to (but stricter than) an Abstract Base Class |
| 2. Automatic Registration | Silently tracks every subclass in a shared list, the moment each is defined | How plugin systems and Django models "discover" new components automatically |
| 3. Auto-Add Attributes/Methods | Injects extra attributes into every class built with it, without the class writing them itself | Automatically tagging or categorizing many related classes at once |

### A follow-up question worth exploring

Use Case 1's `PetMeta` and Use Case 3's `PetMeta` each do only one job. As a follow-up exercise: **write a single, combined `PetMeta` that does both** — refuses to create a class without `speak()` (Use Case 1's behaviour), *and* automatically adds `category = "Animal"` to every class that does pass the check (Use Case 3's behaviour). (Hint: both checks can live inside the same `__new__()` method, one after another — decide which one should run first, and think about whether the order matters here.)

---

## Quick recap

- A **custom metaclass** (built by inheriting from `type`) gets a chance to inspect, validate, or modify a class **at the moment it's being defined** — earlier than anything an Abstract Base Class or `__init_subclass__` hook can do, since those only run once the class already fully exists.
- **Use Case 1** shows a metaclass *rejecting* a class outright if it breaks a rule, by raising an error directly inside `__new__()`.
- **Use Case 2** shows a metaclass *silently registering* every subclass automatically — the metaclass-based sibling of the `__init_subclass__` approach from the earlier registration page, achieving the same practical goal a different way.
- **Use Case 3** shows a metaclass *injecting* new attributes directly into a class's dictionary before the class is finished being built — giving every class built with it shared behaviour "for free."
- **Each `PetMeta` in this chapter only does the specific job shown in its own example** — Use Case 1's version enforces `speak()`; Use Case 3's version adds `category`. Combining both behaviours into one metaclass (as in the follow-up question above) takes a deliberate, explicit design choice.


