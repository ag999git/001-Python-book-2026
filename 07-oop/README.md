
# Chapter 7: Object-Oriented Programming, Part I

The online companion to Chapter 7 of the book. The printed chapter introduces the class: attributes, methods, `self`, `__init__` and the idea that everything in Python is an object. These pages carry the full answers to the questions at the end of the chapter, the scripting exercises, and six research pages that answer the questions the chapter raises but has no room to settle.

By the end of these pages you should be able to say what `self` actually is, explain when an object is destroyed and when it is not, tell a shallow copy from a deep one, and know the difference between `str()` and `repr()` and when each is used.

You need Chapters 5 and 6 (functions) first.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Questions and Answers](010-oop-conceptual-questions.md) | The conceptual questions from the end of the chapter, each answered in full | Start here |
| [Scripting Exercises](011-ch7-scripts.md) | The programming exercises, with complete worked answers | Practice |
| [Proving That self Is the Object Itself](005-id-self-object.md) | A short experiment with `id()` that settles what `self` is, once and for all | Read early |
| [How del and \_\_del\_\_() Really Work](006-ch7-how-del-works.md) | What `del` removes, when `__del__` runs, and why it is not a destructor in the C++ sense | After the chapter's section on objects |
| [str() versus repr()](013-ch7-str-repr.md) | Two ways to turn an object into text, who calls each, and what to write in your own classes | When you first write `__str__` |
| [Implicit Inheritance from object](014-ch7-object.md) | Every class inherits from `object`, and what that gives you for free | After the chapter |

## The Research Pages

These four go past the printed chapter. Read them when the topic comes up rather than in order.

| Page | Question it answers |
| --- | --- |
| [Circular References and the Garbage Collector](007-ch7-research-q1.md) | If two objects point at each other and nothing else points at them, what frees them? |
| [Shallow Copy versus Deep Copy](008-ch7-research-q2.md) | When does copying an object copy what is inside it, and when does it not? |
| [What Is a Memory Leak in Python?](009-ch7-research-q3.md) | Python manages memory for you, so how can a program still run out? |
| [Breaking a Linear Congruential Generator](012-ch7-prng.md) | A worked exercise showing why a simple pseudo-random generator is predictable |

## Suggested Reading Order

1. **Proving That self Is the Object Itself.** It is short, and it removes the single biggest confusion beginners have with classes.
2. **Conceptual Questions and Answers**, in order.
3. **Scripting Exercises.** Write your own answer first, run it, then compare.
4. **str() versus repr()** and **Implicit Inheritance from object**, which explain what your class already has before you write anything.
5. **How del works**, then the three memory research pages together. They are one story told in three parts.
6. **The LCG page** as a project.

## Two Points Worth Extra Care

**`self` is not a keyword.** It is an ordinary parameter that receives the object the method was called on. `dog.speak()` is `Dog.speak(dog)`. The first page proves this with `id()`, and once you have seen it, nothing about methods is mysterious.

**`del x` does not destroy an object.** It removes the name `x`. The object is freed only when nothing at all refers to it, which is why `__del__` may run much later than you expect, or in a different order. The `del` page and the circular-reference page work through what actually happens.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath.

Scripts that print `id()` values, memory addresses, or the output of a random generator will show different numbers on your machine. Only the relationship between the numbers — whether two are equal or different — is meant to match.
