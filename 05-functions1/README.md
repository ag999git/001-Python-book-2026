
# Chapter 5: Functions, Part I

The online companion to Chapter 5 of the book. The printed chapter introduces the function: how to define one, how to call it, how arguments are passed and what `return` does. These pages add the full answers to the questions at the end of the chapter, thirty more conceptual questions, and a reference page on the `math` module.

By the end of these pages you should be able to say exactly what happens when a function is called, explain why every Python function returns something even when you write no `return`, and know where to look in `math` instead of writing the arithmetic yourself.

You need Chapters 1 to 4 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Questions and Answers](003-ch5-functions-qa.md) | The lettered questions from the end of the chapter, each with a full answer and a worked example | Start here |
| [More Conceptual Questions](005-ch5-more-conceptual-qa.md) | Thirty further questions, from the basic syntax through to scope, memory and closures | After the book questions |
| [The math Module](001-ch5-math.md) | The constants and functions `math` gives you, grouped by purpose, with worked problems and the modern alternatives | Reference |
| [Interactive Notebook](000-ch5-colab.md) | Opens this chapter's exercises in Google Colab | Running code in a browser |

## What Is on the math Page


| Section | Covers |
| --- | --- |
| Mathematical constants | `pi`, `e`, `tau`, `inf`, `nan` |
| Number theory and representation | `ceil`, `floor`, `trunc`, `fabs`, `gcd`, `factorial`, `isclose`  |
| Powers and logarithms | `sqrt`, `isqrt`, `pow`, `exp`, `log`, `log10` |
| Trigonometry and angles | `sin`, `cos`, `tan`, `hypot`, `degrees`, `radians` |
| Hyperbolic and special functions | `sinh`, `cosh`, `gamma`, `erf` |
| Worked problems |  Two complete scripts: the hypotenuse of a right triangle and the area of a circle  |
| Modern alternatives | NumPy, SciPy, SymPy and the `decimal` module, and when each does the job better |


## Suggested Reading Order

1. **Questions and Answers**, in order. They follow the printed chapter.
2. **More Conceptual Questions**. The later ones go past the printed chapter into scope and closures; do not worry if those need a second reading.
3. **The math module** as a reference. Skim it once so you know what is there, then come back when you need a particular function.

## Two Points Worth Extra Care

**Every function returns a value.** If you write no `return`, Python returns `None`. That is why `print(hello())` shows `None` under whatever `hello()` printed. Question c on the first page works through it.

**A function is a way of breaking a problem up, not just of saving typing.** The real gain is that each piece can be understood, tested and fixed on its own. The first two questions of both pages are about this, and it is worth taking them seriously rather than skipping to the syntax.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath, so you can check your result.

`math` is part of standard Python, so it needs no install — just `import math`.
