
# Chapter 17: Strings

The online companion to Chapter 17 of the book. The printed chapter introduces the string: how to build one, index it, slice it and clean it. These pages carry the full answers to all forty questions at the end of the chapter, and add a page on dates and times, which are the most common kind of text a real program has to produce and read.

By the end of these pages you should be able to say what happens in memory when you "change" a string, slice any part of one without counting on your fingers, choose the right method for a job from the forty or so a string offers, write an f-string with formatting, and handle a timestamp without silently losing hours.

You need Chapters 1 to 6 first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Questions and Answers](080-ch17-conceptual-qa.md) | The twenty conceptual questions, in five parts, from what a string is through to palindromes | Start here |
| [Scripting Questions and Answers](090-ch17-scripting-qa.md) | Twenty small programs, each with its steps, its real output, and the pattern it shows | After the conceptual page |
| [Beyond the Basics: Timezones, Calendars and Datetimes](050-ch17-assignment-timezone.md) | Naive and aware datetimes, the IANA zone database, `strftime()` and `strptime()`, and three lab assignments | Before you write anything that records a time |

## What Is on the Conceptual Page

| Part | Questions | Topics |
| --- | --- | --- |
| 1. What a String Is | Q1 to Q5 | An ordered sequence; the three kinds of quotes; `str()`; positive and negative indexing; immutability |
| 2. Writing Characters That Are Hard to Type | Q6, Q7 | Escape sequences, and the raw-string prefix |
| 3. Working Through a String | Q8 to Q10 | Traversal with `for` and with `while`; `+`, `*`, `in`; slicing |
| 4. Characters, Comparison, Methods and Formatting | Q11 to Q16 | Unicode, `ord()` and `chr()`; how strings compare; methods as object methods; the common methods; the `is` family; f-strings |
| 5. Palindromes and a Full Review | Q17 to Q20 | Two ways to test a palindrome, when to use each, and a review of the whole chapter |

## What Is on the Scripting Page

The twenty programs are grouped the same way: creating and inspecting a string (Q1 to Q4), traversal, repetition and slicing (Q5 to Q8), characters and comparison (Q9, Q10), the string methods (Q11 to Q17), and negative slicing, conditions and type conversion (Q18 to Q20). The page ends with a one-line summary of all twenty.

## Suggested Reading Order

1. **Conceptual Part 1.** Question 5, on immutability, is the one to get right. Everything else about strings follows from it.
2. **Conceptual Parts 2 and 3**, then the matching scripting questions. Read a conceptual answer, then write the program that uses it.
3. **Conceptual Part 4.** This is the longest part and the one you will come back to. Question 14 is a reference list of the common methods.
4. **The scripting page in full**, as practice. Write your own answer first, run it, then compare.
5. **Conceptual Part 5** for the palindrome problem, which brings indexing, slicing and comparison together.
6. **Timezones and datetimes** last, or whenever you first need to store a time.

## Three Points Worth Extra Care

**A string cannot be changed.** `s.upper()` does not change `s`. It builds a new string and hands it back. If you do not keep the result in a variable, it is lost. Question 5 shows this with `id()`, and Question 13 shows why it catches people out.

**Slicing never raises an error for being out of range.** `"Python"[2:99]` gives `"thon"`, not an error, while `"Python"[99]` does raise one. Question 10 explains the rule.

**A timestamp without a zone is only a clock reading.** Subtracting two naive datetimes taken in different places gives a wrong answer and no error at all. The timezone page works through a case where the result is out by three and a half hours.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Every output shown was produced by running the script above it.

Two cautions. Scripts that use `input()` wait for you to type, so run those in a terminal. On the timezone page, any script that reads the clock will print your date and time, not the one on the page; the shape of the output is what should match. The number of zones in the IANA database also depends on the version installed on your machine.
