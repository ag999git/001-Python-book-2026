# Chapter 4: Flow Control

The online companion to Chapter 4 of the book. The printed chapter covers the three shapes every program is built from: running lines in order, choosing between paths, and repeating work. These pages give the full answers to the questions at the end of the chapter, add forty conceptual questions of their own, and solve the two "Beyond the Text" problems.

By the end of these pages you should be able to read any `if-elif-else` chain and say which branch runs, choose between `while` and `for` without guessing, use `break`, `continue` and the loop `else` correctly, and explain what a `for` loop is really doing behind the scenes.

You need Chapters 1 to 3 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Questions and Answers](03-flow-control-ch4-qa.md) | The twelve lettered questions from the end of the chapter, with worked scripts: truthiness, nested `if`, `do...until`, `pass`, definite and indefinite loops, infinite loops, nested `for`, `while` against `for`, `range()`, short-circuit evaluation and `continue` | Start here |
| [Conceptual Questions and Answers](03-2-ch4-conceptual-qa.md) | Forty questions in four parts, from the foundations through to `match-case`, the iterator protocol, the walrus operator and EAFP | After the book questions |
| [Beyond the Text Solutions](04-ch4-flow-control-beyond-text.md) | Unreachable (dead) code, and writing a loop without using the word `for` | The two chapter projects |
| [Interactive Notebook](00-ch4-colab-nb.md) | Opens this chapter's exercises in Google Colab | Running code in a browser |

## What Is on the Conceptual Page

The forty questions are grouped so that you can read one part at a sitting:

| Part | Questions | Topics |
| --- | --- | --- |
| I. Foundations of Program Flow | Q1 to Q10 | Sequence, selection and iteration; what "truthiness" means and where it misleads you |
| II. Advanced Selection | Q1 to Q10 | The rule of one, why the order of `elif` matters, the dangling `else`, and `match-case` with guards and the wildcard |
| III. Iterative Logic and Loop Control | Q1 to Q10 | `while` against `for`, how `range()` saves memory, `break`, `continue`, `pass`, the loop `else`, and nested loops |
| IV. Beyond the Basics | Q1 to Q10 | The iterator protocol, the walrus operator, dead code, EAFP against LBYL, and the clearer error messages of Python 3.11 |

The page ends with a quick revision summary.

## Suggested Reading Order

1. **Questions and Answers**, the lettered questions, in order. They follow the printed chapter.
2. **Conceptual Part I**, which explains truthiness properly. Question 10 there shows the two traps that catch beginners: a string holding only a space is not empty, and a real value of `0` is falsy.
3. **Conceptual Parts II and III** as the chapter's core. Part III is the one to reread before an exam.
4. **Beyond the Text**, both problems. The second one, writing a loop without `for`, is the best way to see what a `for` loop really does.
5. **Conceptual Part IV** last. It goes past the printed chapter and is easier once the rest is settled.

## Three Points Worth Extra Care

**Only one branch of `if-elif-else` ever runs.** Once a condition is True, Python skips the rest of the chain, however many later conditions are also True. That is why the order of your `elif` lines changes the result.

**`break` and `continue` are not the same kind of jump.** `break` ends the whole loop; `continue` ends only the current round. The loop's `else` block runs after a natural finish but is skipped after a `break`.

**Python has no `do...until`.** The usual replacement is `while True` with a `break` at the point where you would have put the `until`. Question d on the first page and Question 5 of Part III both show it.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath, so you can check your result.

Two cautions. Scripts that ask for input with `input()` will wait for you to type something; run those in a terminal rather than pasting them into a page that cannot accept typing. The infinite-loop examples have a safety counter added so that they stop on their own instead of running forever.

