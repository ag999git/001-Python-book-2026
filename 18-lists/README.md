
# Chapter 18: Lists

The online companion to Chapter 18 of the book. The printed chapter explains what a list is, how to build one, how to walk through it and which methods it offers. This page takes the next step: fifty-two questions with full answers, worked scripts and diagrams.

By the end of these pages you should be able to slice a list without counting on your fingers, explain why two names can point to one list and what goes wrong when you forget it, write a list comprehension instead of a four-line loop, and handle a matrix stored as a list of lists.

You need Chapters 1 to 6 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Questions and Answers](50-ch18-qa.md) | Fifty-two questions in eight sections, from what a container is through to random sampling. Every answer has steps, a script and its real output | The whole chapter |

This chapter has a single page, but it is a long one. The table below is a map of it.

## What Is on the Page

| Section | Questions | Topics |
| --- | --- | --- |
| General Concepts | Q1 to Q7 | Containers, sequences and mappings; why a string cannot be changed and a list can; negative indexing; iterables; `+` on lists; when a list counts as True |
| Slicing | Q8 to Q10 | The slice formula, reversing with a slice, and what negative start and stop values do |
| Assignment, Copying and Aliasing | Q11 to Q15 | The difference between `b = a` and `b = a.copy()`, the bugs aliasing causes, `[:]` against `.copy()`, why `[[0] * 3] * 4` is not four rows, and deep copying |
| List Methods and Common Gotchas | Q16 to Q21 | What `sort()` returns, three expressions that fail, `append` against `extend`, `del`, sorting tuples by a key, and the mutable default argument |
| List Comprehension | Q22 to Q28 | Flattening, filtering, pairing with `zip`, and unpacking |
| Exercises | Q29 to Q45 | Seventeen small complete problems, from removing duplicates to evaluating a polynomial |
| Matrices | Q46 to Q48 | A list of lists, and transposing one |
| Randomization | Q49 to Q52 | Random samples, differences between consecutive numbers, reversing without a slice, and sampling without replacement |

The page opens with a glossary and a map of Python's containers, and closes with a table of common mistakes and a list of further reading.

## Suggested Reading Order

Work through the page in order the first time. The sections build on each other: copying is easier to follow once slicing is clear, and the exercises lean on both.

If you are short of time, these are the questions that change how you write Python:

1. **Q11 to Q15, on copying and aliasing.** This is the most important group on the page. A list is an object, and a name is only a tag tied to it. Almost every list bug a beginner meets comes from forgetting that.
2. **Q21, the mutable default argument.** A default value is built once, when the `def` line runs, not once per call. This one surprises experienced programmers too.
3. **Q8, the slice formula.** Learn it once and slicing stops being guesswork.
4. **Q22 to Q28, comprehensions.** They will shorten almost every loop you write from here on.

## Two Points Worth Extra Care

**`b = a` does not make a copy.** It gives the same list a second name. Change it through either name and both see the change. Q11 and Q12 show this with `id()`; Q13 shows the two ways to make a real copy, and Q15 shows when even those are not enough.

**`[[0] * 3] * 4` gives one row, stored four times.** Set a value in the first row and it appears in all four. Q14 shows why, and the list comprehension that fixes it.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Every output on the page was produced by actually running the script above it.

The randomization questions are the exception. Those scripts use random numbers with no fixed seed, so your numbers will differ from the ones printed. Only the shape of the result is meant to match.
