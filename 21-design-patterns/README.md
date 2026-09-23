# Chapter 21: Design Patterns

The online companion to Chapter 21 of the book. A design pattern is a tried and tested shape for solving a problem that keeps coming back. It is not an algorithm and not ready-made code: it is a plan you adapt. These pages carry the full answers to all forty questions at the end of the chapter, twenty conceptual and twenty scripting.

By the end of these pages you should be able to name the three families of patterns and say what each is for, recognise the handful you will actually meet in Python code, write each of them, and — just as important — know when a pattern is not needed at all.

You need Chapters 7 and 8 (object-oriented programming) first. Some answers also use decorators, context managers and dataclasses.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Questions and Answers](060-ch21-conceptualqa.md) | Twenty questions: what a pattern is, the three families, each pattern in turn, how to choose one, and the anti-patterns to avoid | Start here |
| [Scripting Questions and Answers](080-ch21-scriptsqa.md) | Twenty complete programs, one for each pattern, with output and an explanation | After the conceptual page |

## The Patterns Covered

| Family | Patterns | Where |
| --- | --- | --- |
| Creational — how objects are made | Singleton, Factory Method, Abstract Factory, Builder, Prototype | Conceptual Q3, Q4, Q6, Q7; scripts Q1 to Q5 |
| Structural — how objects are put together | Decorator, Adapter, Facade, Composite, Proxy | Conceptual Q5, Q8 to Q12; scripts Q6 to Q11 |
| Behavioral — how objects talk to each other | Observer, Strategy, Command, Iterator, Template Method | Conceptual Q13 to Q16; scripts Q12 to Q16 |
| Pythonic alternatives | Decorators, context managers, mixins, duck typing, dataclasses | Conceptual Q17; scripts Q17 to Q20 |

Three questions stand apart from the catalogue and are worth reading whatever else you skip:

- **Q17, Pythonic design patterns.** Several classical patterns are already built into Python. A decorator does the Decorator pattern. A `with` block does resource management. `@dataclass` gives you a value object in one line. Writing the classical version by hand is often the wrong choice in Python.
- **Q18, choosing a pattern.** The first question is always whether a plain function would do.
- **Q20, anti-patterns.** Over-engineering, the God Object, and cargo-cult programming — copying a pattern because it looks professional rather than because it solves your problem.

## Suggested Reading Order

1. **Conceptual Q1 and Q2** for what a pattern is and how the three families differ.
2. **Conceptual Q18**, out of order, before you learn any pattern in detail. It sets the right frame of mind: a pattern is a last resort, not a first move.
3. **The patterns themselves**, family by family, reading the conceptual answer and then writing the matching script.
4. **Conceptual Q17** once you have written a few by hand, so you can see how much Python gives you for free.
5. **Conceptual Q19 and Q20** at the end.

## Two Points Worth Extra Care

**A pattern is a plan, not a library.** There is no `import singleton`. Each of these is a way of arranging classes and calls that you write yourself, and you adapt it to the problem in front of you.

**The Pythonic version is usually the right one.** Question 5 compares the classical Decorator class with Python's `@` syntax; question 17 does the same for four more patterns. Reach for the language feature first and the classical pattern only when the feature does not fit.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Every output shown was produced by running the script above it.

The short snippets inside the follow-up questions are the exception. Those are fragments that extend a class from the main script above them, so run that script first.

