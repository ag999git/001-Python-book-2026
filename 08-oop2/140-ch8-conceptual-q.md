


# Chapter 8.140 — 30 Conceptual Questions & Answers: A Full OOP Review

## What this page covers

This page is a comprehensive review, pulling together concepts from across this chapter and the previous one — inheritance, MRO, `super()`, namespaces, composition, and abstract methods — into thirty focused question-and-answer pairs. Think of it less as new material and more as a checkpoint: if you can confidently answer all thirty questions in your own words, it's a strong sign that the individual chapter pages on these topics have connected into a coherent understanding, rather than staying as isolated facts.

The questions themselves are fixed, exactly as printed in the book. The answers below have been expanded from the original one-liners into fuller explanations — with short logical steps wherever a question describes a process, plain-language definitions of any technical term, and links back to the specific earlier chapter pages (or, where more useful, to Python's official documentation) that cover each topic in full depth.

---

**1. What is the fundamental goal of inheritance in Python?**

The primary goal of inheritance is **code reusability**. It lets a child class reuse and extend logic already written in a parent class, without rewriting that logic from scratch. This is a direct application of the DRY ("Don't Repeat Yourself") principle — see the earlier chapter page, "The Eleven Properties of Inheritance," for a full breakdown of code reuse alongside inheritance's other benefits. ([Python docs: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance))

---

**2. Which built-in class sits at the very top of the Python class hierarchy?**

The `object` class is the root of all classes in Python — every class you create automatically inherits from it, whether you write that inheritance explicitly (`class Dog(object):`) or leave it implicit (`class Dog:`, which means exactly the same thing in Python 3). See the earlier chapter page, "Implicit Inheritance from `object`," for the full explanation and a hands-on script proving this for both custom classes and built-in types like `int` and `str`.

---

**3. Define the "Is-A" relationship in the context of OOP.**

An "Is-A" relationship is a structural link where a subclass is a *specific type* of its superclass — for example, "a `Dog` is-a `Pet`." This relationship is what inheritance actually models; it's directly confirmed in code using `isinstance()` and `issubclass()`, both covered in the earlier Animal Management System page.

---

**4. What happens if you define a child class using the `pass` keyword?**

The child class becomes an exact clone of the parent class — it inherits every attribute and method the parent has, without adding or changing anything of its own.

```python
class Pet:
    def speak(self):
        print("Some generic sound")

class Dog(Pet):
    pass   # Dog adds NOTHING new -- it behaves 100% like Pet, for now

d = Dog()
d.speak()   # -> Some generic sound (inherited directly, unchanged)
```

This pattern is genuinely useful — see Question 26 below for a specific real-world reason a developer might deliberately do this.

---

**5. What is the difference between Single Inheritance and Multiple Inheritance?**

**Single inheritance** involves exactly one parent class (e.g., `class Dog(Pet):`). **Multiple inheritance** allows a child class to inherit from more than one immediate parent class at once (e.g., `class Amphibian(Walker, Swimmer):`), covered in depth in the earlier chapter page, "`super()` in Multiple Inheritance and the Diamond Problem."

| | Single Inheritance | Multiple Inheritance |
|---|---|---|
| Number of direct parents | One | Two or more |
| Example | `class Dog(Pet):` | `class Amphibian(Walker, Swimmer):` |
| Main added complexity | None beyond ordinary inheritance | Requires understanding the MRO (see Questions 8–13) |

---

**6. Explain the concept of "Transitivity" in inheritance.**

Transitivity means inheritance "passes through" multiple levels automatically: if Class `B` inherits from Class `A`, and Class `C` inherits from Class `B`, then Class `C` automatically possesses everything Class `A` provides too, even though `C` never mentions `A` directly.

![Flowchart](/resources/ch-8-august-2026-conceptual-question-6.png)



`C` inherits from `B`, and `B` inherits from `A` — so `C` transitively has access to everything `A` originally defined, even without a direct line connecting `A` and `C`.

---

**7. What is Method Overriding?**

Overriding occurs when a child class provides its *own* implementation of a method that already exists on its parent, replacing the parent's version specifically for objects of the child class. This is covered extensively in the earlier "Eleven Properties of Inheritance" and Animal Management System pages, where `Dog.speak()` and `Cat.speak()` both override a shared parent's generic `speak()`.

---

**8. What does MRO stand for, and what is its purpose?**

MRO stands for **Method Resolution Order**. It's the exact, deterministic order Python follows when searching for a method or attribute through a class's ancestry — guaranteeing that, no matter how complicated a class hierarchy gets, Python always knows precisely which version of a method to run. ([Python docs: `__mro__`](https://docs.python.org/3/library/stdtypes.html#class.__mro__))

---

**9. In a standard class hierarchy, where does the MRO search always end?**

The MRO search always ends at the built-in `object` class — every class's ancestry, no matter how deep, eventually converges there, as covered in Question 2 above and the earlier "Implicit Inheritance from `object`" page.

---

**10. What is the default behaviour of the `__str__` method inherited from the `object` class?**

By default, it returns a string containing the class name and the object's memory address, in the form `<ClassName object at 0x...>`. This default is used automatically by `print()`/`str()` whenever a class doesn't define its own `__str__()` *or* `__repr__()` — see the earlier chapter page, "`str()` versus `repr()`," for the full set of fallback rules governing exactly when this default actually gets used.

---

**11. Why is the `super()` function used?**

`super()` is used to call a method from the parent class (or, more precisely, from the next class in the MRO) from inside a child class's own method — allowing the child to reuse and build on the parent's logic, rather than duplicating or fully replacing it. See Question 12 for an important clarification on exactly *which* class `super()` actually reaches.

---

**12. Does `super()` always call the immediate parent class?**

**Not necessarily.** In multiple inheritance, `super()` follows the Method Resolution Order (MRO) — which might lead to a "sibling" class (another parent listed alongside the immediate one) before it eventually reaches what you might intuitively think of as "the" parent. This is the single most important and most commonly misunderstood idea covered in the earlier "diamond problem" chapter page — `super()` means "next in the MRO," never simply "my parent."

---

**13. What is the "Depth-First, Left-to-Right" rule?**

It's the basic logic Python's MRO calculation uses when resolving multiple inheritance: Python fully searches the leftmost parent (and that parent's *entire* ancestry) before moving on to the next parent listed to its right.


![Flowchart](/resources/ch-8-august-2026-conceptual-question-13.png)



This is exactly why `class Dog1(Walker, Swimmer):` and `class Dog2(Swimmer, Walker):` — covered in the earlier diamond-problem page — end up with genuinely different, mirror-image MROs: Python simply reads the parent list left to right, and follows each one's full chain before continuing to the next name.

---

**14. What is a "Namespace" in Python?**

A namespace is a container (technically implemented as a dictionary) that maps variable names (the keys) to the actual objects they refer to (the values). See the earlier chapter page, "Namespaces: `__dict__` and the LEGB Rule," for the full picture.

---

**15. List the four levels of the LEGB rule for namespaces.**

**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in. Python checks these four scopes, in exactly this order, whenever it needs to resolve a variable name — see the earlier LEGB chapter page for a full worked script demonstrating all four levels, plus `global` and `nonlocal`.

---

**16. What information do the `locals()` and `globals()` functions provide?**

They return real, inspectable dictionaries containing every variable currently available in the local scope (`locals()`) and the global/module scope (`globals()`) respectively — turning the otherwise-invisible idea of a "namespace" into something you can actually print and examine. ([Python docs: `locals()`](https://docs.python.org/3/library/functions.html#locals), [`globals()`](https://docs.python.org/3/library/functions.html#globals))

---

**17. How can you access the namespace dictionary of a class or an instance?**

Using the `__dict__` attribute — `SomeClass.__dict__` for the class's own namespace, or `some_instance.__dict__` for that specific object's namespace. Covered fully in the earlier `__dict__` chapter page, including how to add or modify attributes by editing `__dict__` directly.

---

**18. Are the namespaces of a Class and its Instance the same?**

**No.** A class has its own namespace, containing class variables and method definitions; each individual instance has its own *separate* namespace, containing only that specific object's instance attributes. See Question 6 in the earlier "OOP Conceptual Questions" page for the class-variable-vs-instance-variable distinction this relies on.

---

**19. Define "Composition" (the "Has-A" relationship).**

Composition is when one class contains an instance of another class as an attribute, implying *ownership* rather than a type relationship — for example, "a `Dog` has-a `Collar`." This is the strongest of the three Has-A relationships covered in the earlier chapter page, "Has-A Relationships: Composition, Aggregation, and Dependency," which also covers the two weaker variants (Aggregation and Dependency) for comparison.

---

**20. What is an Abstract Method?**

An abstract method is a placeholder method, declared in a parent class, with no real implementation of its own — its purpose is to *force* every subclass to provide its own specific version, or Python will refuse to let that subclass be instantiated at all (when combined with `ABC`, as covered in the earlier Animal Management System and Robust Pet System pages).

---

**21. How do you informally create an abstract method in Python?**

By defining a regular method in the parent class that simply contains `raise NotImplementedError("message")`. This is a **weaker** form of enforcement than a true `ABC`-based abstract method — nothing stops you from creating an object of the incomplete subclass; the error only appears later, at the moment the missing method is actually *called*, rather than immediately at object creation. (See the earlier "Robust Pet System" chapter page's comparison table between this approach and the `ABC` module for the full trade-off.)

```python
class Pet:
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class IncompletePet(Pet):
    pass   # No error here! The class is created just fine...

p = IncompletePet()   # ...and so is the object.
# p.speak()   # ...but THIS line would raise NotImplementedError,
              # only once you actually try to use the missing method.
```

---

**22. What is "Multilevel Inheritance"?**

A chain of inheritance where a class is derived from another *derived* class — for example, `Grandchild` inherits from `Child`, which itself inherits from `Parent`. This is exactly the pattern behind Question 6's "transitivity" concept above.

---

**23. What is "Hierarchical Inheritance"?**

A structure where a single parent class serves as the base for *multiple* different, independent subclasses — for example, `Pet` being the shared parent for both `Dog` and `Cat`, as seen throughout this chapter's `Pet`/`Dog`/`Cat` examples.

![Flowchart](/resources/ch-8-august-2026-conceptual-question-23.png)



---

**24. Explain "Cooperative Is-A" (Refinement).**

This is a pattern where a child class uses `super()` to let the parent handle part of a task, while the child adds its own specialized logic on top of (rather than instead of) the parent's behaviour. `Dog.walk()` in the earlier "Eleven Properties of Inheritance" page is a direct example: it prints its own dog-specific message, and *then* calls `super().walk()` to also run the parent's original logic, rather than replacing it outright.

---

**25. What is "Replacement Is-A" (Total Overriding)?**

This is when a child class completely ignores the parent's logic for a particular method and provides an entirely different implementation instead — no `super()` call at all. `Dog.speak()` and `Cat.speak()` throughout this chapter are examples: neither calls `super().speak()`; each simply replaces the parent's generic version outright.

---

**26. Why would a developer use `class Admin(User): pass`?**

This is an "Implicit Is-A" (pass-through) pattern, used to create a **semantically distinct role** in code, even though the underlying data and behaviour are, for now, identical to the parent. It signals intent — "an `Admin` is conceptually a special *kind* of `User`" — and leaves the door open to add admin-specific behaviour later, without needing to restructure anything that already depends on `Admin` being a `User`.

---

**27. What happens if a child class defines an `__init__` method but does not call `super().__init__()`?**

The parent's constructor is never called at all, and any attributes the parent's `__init__` would normally have set up simply won't exist on the child object — which can cause confusing `AttributeError`s later, whenever code tries to access an attribute that was only ever supposed to be set up by the parent. This is exactly why "constructor chaining" via `super().__init__()` is emphasized so consistently throughout this chapter's scripts (see the earlier "Eleven Properties of Inheritance" and Animal Management System pages).

---

**28. How does Python link variable names to objects internally?**

Python identifies every object with a unique `id()` (its memory address — see the earlier chapter page, "Proving That `self` Is Just the Object Itself," for a hands-on demonstration), and a namespace dictionary maps each variable name to the `id()` of the object it currently refers to.

---

**29. What is the benefit of Composition over Inheritance?**

Composition offers more flexibility, because it lets you combine functionality from *multiple, unrelated* sources freely, without being constrained by a rigid class hierarchy — you're simply storing an object as an attribute, rather than needing that object's class to fit into an "is-a" relationship at all. This trade-off is explored directly in the earlier "Has-A Relationships" chapter page's follow-up question about `Car`/`Engine`, and is often summarized by the design principle **"favor composition over inheritance."** ([Wikipedia: Composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance))

---

**30. What is "Hybrid Inheritance"?**

Hybrid inheritance is simply a combination of two or more of the inheritance patterns already covered above — for example, mixing multiple inheritance (Question 5) with multilevel inheritance (Question 22) in the same overall class hierarchy. There's no single fixed shape to a hybrid hierarchy; the name just describes "more than one pattern, combined."

---

## Summary map: how these thirty questions connect

| Theme | Questions | Covered in depth on |
|---|---|---|
| Basic inheritance & Is-A | 1, 3, 4, 5, 22, 23, 26, 30 | Earlier Animal Management System & "Eleven Properties" pages |
| `object`, MRO, `super()` | 2, 8, 9, 11, 12, 13 | "Implicit Inheritance from `object`" & "Diamond Problem" pages |
| Namespaces & scope | 14, 15, 16, 17, 18, 28 | "`__dict__` and the LEGB Rule" page |
| Overriding patterns | 6, 7, 24, 25, 27 | "Eleven Properties of Inheritance" page |
| Abstraction & composition | 19, 20, 21, 29 | "Has-A Relationships" & "Robust Pet System" pages |
| Special methods | 10 | "`str()` versus `repr()`" page |

## Quick recap

- These thirty questions cover **four broad themes**: inheritance mechanics (Is-A, MRO, `super()`), namespaces and scope (LEGB, `__dict__`), design patterns for overriding (cooperative vs. replacement), and composition/abstraction (Has-A relationships, abstract methods).
- The single idea that ties the most questions together is probably **Question 12**: `super()` follows the MRO, not a fixed "parent" — this single correction underlies Questions 8, 9, 11, 13, and 24 as well.
- If any single answer above still feels unclear, the "Covered in depth on" column in the summary table points directly to the specific earlier chapter page that develops that idea with full worked examples and diagrams.





