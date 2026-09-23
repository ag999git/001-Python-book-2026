# Chapter 3: Operators in Python

The online companion to Chapter 3 of the book. The printed chapter introduces the operators you will use in almost every line of Python: arithmetic, assignment, comparison, logical, membership and identity. These pages give the full answers to the questions at the end of the chapter, and add two operators the printed chapter does not have room for.

By the end of these pages you should know why `=` is not the "equals" sign of mathematics, what `is` tests that `==` does not, how floor division and the remainder operator behave when a negative number is involved, and how the `@` and set operators work.

You need Chapter 1 and Chapter 2 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Questions and Answers](001-ch3-qa.md) | The eleven lettered questions from the end of the chapter, each with a full answer, a script you can run, and the output | Start here |
| [Beyond the Text: Matrix Multiplication and Set Operators](003-ch3-beyond-text.md) | The `@` operator with NumPy, and the four set operators `\|`, `&`, `-` and `^` | After the questions |
| [Interactive Notebook](004-Ch3-colabnb.md) | Opens this chapter's exercises in Google Colab | Running code in a browser |

## What Is on the Questions Page

The questions follow the lettering of the printed book:

| Question | Topic |
| --- | --- |
| a, b | Assignment, and why `=` is not the mathematical "equals to" |
| c | Membership operators `in` and `not in` |
| d | The difference between `==` and `is` |
| e | Why you can assign to a variable but not to a literal |
| f | Floor division `//` |
| g | The sign of the remainder when the divisor is negative |
| h | The six comparison operators |
| i | Identity and membership operators together |
| j | Why object identity matters |
| k | The care needed with `%` on negative numbers |

The page opens with a short table of key terms (object, binding, literal, operand, dividend, divisor, quotient, remainder) so that no word in the answers is a surprise. It ends with a summary table and one practice script that puts everything together.

## Suggested Reading Order

1. **Questions a to e.** These build the single most important idea in the chapter: a name in Python points to an object, it does not contain one. Everything about `is`, `==` and `id()` follows from it.
2. **Questions f, g and k** as one sitting. Floor division and the remainder operator are a single rule seen from two sides, and the negative-number cases confuse almost everyone the first time.
3. **Questions h, i and j** for revision.
4. **Beyond the Text** last. The `@` section needs NumPy installed; the set operators section needs nothing extra.

## Two Points Worth Extra Care

**`is` is not a faster `==`.** Two lists with the same contents are equal but are not the same object. Question d shows this with `id()`, and question j shows what goes wrong when you forget it.

**The remainder takes the sign of the divisor.** In Python, `7 % -3` is `-2`, not `1`. This is not a quirk; it follows from `//` always rounding down. Question g works the arithmetic out one step at a time.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath, so you can check your result.

The `@` operator section needs NumPy, which does not come with Python. Install it once with `pip install numpy`. If you use Anaconda, Google Colab or Jupyter, NumPy is already there.

