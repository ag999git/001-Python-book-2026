
# Chapter 6: Functions, Part II

The online companion to Chapter 6 of the book. Where Chapter 5 introduced the function, this chapter takes it further: recursion, the five kinds of parameter, `lambda`, `map()`, `filter()`, `zip()`, generators and decorators. These pages carry the full answers to all thirty-four questions at the end of the chapter, plus separate pages on the topics that need more room.

By the end of these pages you should be able to write a recursive function and say why it stops, choose between a loop and `map()` without guessing, write a generator instead of building a list you do not need, and write a decorator that does not break the function it wraps.

You need Chapter 5 first.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Questions and Answers](008-ch6-q-a.md) | All thirty-four questions from the end of the chapter: arguments and parameters, the five parameter types, `*args` and `**kwargs`, recursion, memoization, the functional tools, generators, and a set of worked programs | Start here |
| [zip(), lambda, map() and filter()](006-ch6-zip.md) | The four functional tools, one at a time, then combined | After questions 10 to 15 |
| [Advanced Generators](007-ch6-generators-advanced.md) | What happens when a generator finishes, how `for` drives one, and two worked generators | After questions 16 and 17 |
| [functools.wraps in Decorators](009-ch6-functools-decorators.md) | Why a decorator quietly loses the name and docstring of the function it wraps, and the one line that fixes it | When you write your first decorator |
| [Additional Problems on Recursion](004-ch6-additional-recursion-problems.md) | Five worked recursive problems: powers, palindromes, GCD, Tower of Hanoi, and testing for even | Practice |
| [Beyond the Text: Research Tasks](005-beyond-text-ch6-functions2.md) | Eight open-ended tasks, from reading real library source to writing a pseudo-random generator | Going further |
| [Interactive Notebook](001-ch6-colab.md) | Opens this chapter's exercises in Google Colab | Running code in a browser |

## What Is on the Questions Page

| Questions | Topic |
| --- | --- |
| 1 to 5 | How arguments are passed, arguments against parameters, lambda, and the five kinds of parameter |
| 6 to 9 | Looping styles, the module search path, the three laws of recursion, and memoization |
| 10 to 15 | `*args`, `**kwargs`, `zip()`, anonymous functions, `map()`, `filter()` |
| 16, 17 | Generator functions and generator iterators, and why they are worth using |
| 18 to 34 | Seventeen worked programs, including the quadratic formula, numerical integration by the trapezoidal rule, the power set, and recursion without the `*` operator |

## Suggested Reading Order

1. **Questions 1 to 9.** Question 5, on the five kinds of parameter, is the one to learn properly — positional, keyword, default, `*args` and `**kwargs` — because every later page uses them.
2. **Questions 10 to 15**, then the **zip, lambda, map and filter** page, which covers the same ground more slowly.
3. **Questions 16 and 17**, then the **Advanced Generators** page.
4. **Additional Problems on Recursion.** The Tower of Hanoi is the classic; work it by hand for three discs before reading the answer.
5. **functools.wraps** when you first write a decorator.
6. **Beyond the Text** last, as project work rather than reading.

## Three Points Worth Extra Care

**Recursion needs a base case, and the recursive call must move towards it.** The three laws in question 8 say this precisely. A recursive function without a base case does not loop forever in Python; it raises `RecursionError`.

**`map()` and `filter()` return an iterator, not a list.** Printing one shows something like `<map object at 0x...>`. Wrap it in `list()` to see the values.

**A decorator replaces your function with a different one.** Without `functools.wraps`, the new function carries the wrapper's name and docstring, so `help()` and debugging show the wrong thing. It is one line to fix and easy to forget.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath.

Two cautions. Scripts that print the address of an object, such as `<map object at 0x...>`, will show a different number on your machine. And the pseudo-random generator in the research tasks is there to show how such a generator works, not for anything that needs real randomness.
