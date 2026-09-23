
# Chapter 2: Python Basics II

The online companion to Chapter 2 of the book. The printed chapter introduces Python's data types. These pages take the numeric types much further than the book has room for, and carry full answers to every question at the end of the chapter.

By the end of these pages you should understand why Python integers never overflow, why `0.1 + 0.2` does not give `0.3`, how complex numbers work in Python, and how to install and manage the packages your own projects will need.

You need Chapter 1 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Python Integers](001-ch2-python-data-types.md) | Why Python integers have no size limit, the arithmetic and bitwise operators, how left shift works, and converting other values to `int` | Start here |
| [Python Floating-Point Numbers](002-ch2-float-data.md) | Notes on how floats really store values, worked example scripts, and a quiz. Explains the `0.1 + 0.2` surprise | After integers |
| [Complex Numbers: A Beginner's Guide](003-ch2-complex-numbers-basics.md) | What a complex number is, why Python has one built in, and the basic operations | If your course covers them |
| [Complex Numbers: An Advanced Guide](004-ch2-complex-numbers-advanced.md) | The `cmath` module, polar form, and worked examples that go past the basics | After the beginner's guide |
| [More Conceptual Questions](005-2-ch2-more-conceptual-qa.md) | Forty questions on *why* Python behaves as it does: mutability, truth values, dictionaries, sets, `None`, modules | Revision |
| [Script Writing Questions and Answers](005-3-ch2-scripting-qa.md) | Forty questions that ask you to write the code, with complete answers | Practice |
| [End-of-Chapter Questions and Answers](005-ch2-book-end-qa.md) | Full answers to the lettered questions (a to v) printed at the end of the chapter | Revision |
| [Installing and Managing Packages with pip and uv](006-beyond-text.md) | `pip`, the faster `uv`, and what `requirements.txt` is for. Beyond the printed chapter | Before your own projects |
| [Interactive Notebook](colab-link.md) | Opens this chapter's exercises in Google Colab | Running code in a browser |

## Suggested Reading Order

1. **Integers**, then **Floating-Point Numbers**. These two carry most of the chapter's weight, and the float page explains a result that puzzles nearly everyone.
2. **Complex Numbers**, beginner's guide first, then the advanced one. Skip both if your syllabus does not include them; nothing later depends on them.
3. **Conceptual**, **Script Writing** and **End-of-Chapter Questions** for revision and practice. Try each question before reading its answer.
4. **pip and uv** when you start writing programs of your own that need outside packages.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath, so you can check your result.

A caution on the float page: a few outputs show long trails of digits, such as `0.30000000000000004`. These are not typing mistakes. They are the point of that section.
