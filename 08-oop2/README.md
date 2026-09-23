# Chapter 8: Object-Oriented Programming, Part II

The online companion to Chapter 8 of the book. Where Chapter 7 introduced the class, this chapter builds with it: inheritance, composition, abstract classes, properties, class and static methods, namespaces, `__slots__` and metaclasses. These pages carry a hundred questions with full answers, and a series of projects that build one system — a pet management program — a piece at a time.

By the end of these pages you should be able to choose between inheritance and composition rather than reaching for inheritance by habit, use `super()` correctly when more than one parent is involved, write a property instead of a getter and a setter, and read a class that uses a metaclass without alarm.

You need Chapter 7 first.

## The Question Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [30 Conceptual Questions](140-ch8-conceptual-q.md) | A full review of object-oriented Python | Start here |
| [30 More Conceptual Questions](145-ch8-more-conceptual-q.md) | Inheritance and namespaces in depth | After the first set |
| [20 Scripting Questions](150-ch8-scripts-q.md) | Programs to write, with worked answers | Practice |
| [20 More Scripting Scenarios](155-ch8-more-scripts.md) | Longer, more realistic problems | After the first set |

## The Topic Pages

| Page | What it covers |
| --- | --- |
| [The Eleven Properties of Inheritance](030-08-ch8-inheritence-properties.md) | What a subclass inherits, what it does not, and what it can change |
| [Has-A Relationships](035-ch8-composition-basics.md) | Composition, aggregation and dependency, and how each differs from inheritance |
| [super() and the Diamond Problem](050-ch8-multiple-inherit-super.md) | What happens when two parents share a grandparent, and how Python decides the order |
| [\_\_new\_\_() versus \_\_init\_\_()](080-ch8-new-init.md) | Which one makes the object and which one sets it up |
| [Namespaces: \_\_dict\_\_ and LEGB](100-ch8-namespace-legb.md) | Where Python looks for a name, and where attributes actually live |
| [Instance, Class and Static Methods](110-ch8-deco-class-static.md) | The three kinds of method and when each is right |
| [Inspecting object's Built-in Methods](020-08-ch8-object-methods.md) | An exercise in looking at what every class already has |
| [Metaclasses, Part 1](090-ch8-type.md) | What `type` really is, and what a metaclass does |
| [Metaclasses, Part 2](091-ch8-type-usecases.md) | The few cases where one is the right tool |

## The Projects

These build on each other and are best done in order.

| Project | What you build |
| --- | --- |
| [Animal Management System](010-08-ch8-rq-animal-system.md) | Inheritance in practice, from a single base class |
| [Composition, Aggregation and Dependency](040-ch8-composition.md) | The same pet system built three ways, so the differences are visible |
| [A Robust Pet System with Abstract Classes](060-ch8-abstract.md) | Using `ABC` so an incomplete subclass fails early instead of at run time |
| [Three Ways to Build Pet Registration](070-ch8-registration.md) | Comparing three designs for the same requirement |
| [Property Decorators](120-ch8-property-deco.md) | Replacing getters and setters with `@property` |
| [Optimizing Pet Objects with \_\_slots\_\_](130-ch8-slots.md) | Cutting memory use, and what you give up in return |

## Suggested Reading Order

1. **The Eleven Properties of Inheritance**, then the **Animal Management System** project.
2. **Has-A Relationships**, then the **Composition** project. Take this pair seriously: choosing composition where inheritance does not fit is the single most useful judgement in this chapter.
3. **super() and the Diamond Problem**, and the **Abstract Classes** project.
4. **Instance, Class and Static Methods**, then **Property Decorators**.
5. **Namespaces** and **\_\_new\_\_ versus \_\_init\_\_** when you want to know how it all works underneath.
6. **\_\_slots\_\_** and the two **Metaclasses** pages last. Neither is needed for ordinary work, but both explain things you will see in other people's code.
7. **The four question pages** for revision and practice throughout.

## Two Points Worth Extra Care

**Inheritance says "is a", composition says "has a".** A `Dog` is an `Animal`, so inheritance fits. A `Car` has an `Engine`; it is not a kind of engine, so composition fits. Inheriting where you should have composed is the commonest design mistake in this chapter.

**`super()` does not simply mean "my parent".** With more than one parent, it follows the method resolution order, which is why the diamond problem has a definite answer in Python. The `super()` page shows the order with `__mro__`.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath.

The `__slots__` page measures memory with `sys.getsizeof()` and similar tools; those numbers depend on your Python version and platform, so only the size of the saving is meant to match.

