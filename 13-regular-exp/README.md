
# Chapter 13: Regular Expressions

The online companion to Chapter 13 of the book. A regular expression is a small language for describing patterns in text: an email address, a date, a password that meets your rules. The printed chapter introduces the `re` module and the pattern syntax. These pages carry twenty-six conceptual questions, forty-two script questions, twenty practice programs, and a set of projects that push the idea further than you would expect it to go.

By the end of these pages you should be able to read a pattern someone else wrote, write one of your own without trial and error, know when a group should capture and when it should not, and — just as important — recognise the jobs a regular expression should not be used for.

You need Chapter 17 (Strings) first.

## The Main Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Regular Expressions in Python: the re Module](10-ch13-re.md) | The full companion to the chapter: the syntax, every `re` function, and worked examples throughout | Start here |
| [Conceptual Questions](50-ch13-re-conceptual-qa.md) | Twenty-six questions on how matching actually works | After the main page |
| [Script-Based Questions and Answers](70-ch13-re-script-qa.md) | Forty-two questions that ask you to write the pattern and the code | Practice |
| [Twenty Regular Expression Programs](98-ch13-script-qa.md) | A graded practice set: digits, emails, dates, hashtags, backreferences, greedy matching and more | Practice |

## Topic Pages

| Page | What it covers |
| --- | --- |
| [Capturing versus Non-Capturing Groups](60-ch13-re-capturing-noncapturing.md) | What `( )` costs you, what `(?: )` saves, and when each is right |
| [The Pattern and Match Classes](80-ch13-pattern-match-class-deepdive.md) | What `re.compile()` hands back, what a match object really is, and why the classes are hidden |
| [Naming Styles: snake_case, camelCase, PascalCase](75-ch13-naming-styles.md) | Converting between the naming conventions with regular expressions |

## Projects

| Project | What it investigates |
| --- | --- |
| [Detecting Prime Numbers Without Arithmetic](90-ch13-prime-numbers.md) | A famous pattern that tests primality by matching, with no division at all |
| [Validating a Password with One Expression](95-ch13-password.md) | Lookahead assertions, and how several rules fit into a single pattern |

## Suggested Reading Order

1. **The main companion page**, in order. It is long, so take it in sittings: the syntax first, then the `re` functions, then the examples.
2. **Conceptual Questions.** These are where the idea of backtracking and greediness becomes concrete.
3. **Capturing versus Non-Capturing Groups.** Short, and it fixes a habit before it forms.
4. **The two script sets** as practice. Write your own pattern first, test it, then compare.
5. **The Pattern and Match classes** when you start compiling patterns for reuse.
6. **The password project**, then the **prime numbers** one. The second is a curiosity rather than something to copy, and it is more fun once the first has shown what lookahead does.

## Three Points Worth Extra Care

**Quantifiers are greedy by default.** `<.*>` on `<a><b>` matches the whole string, not just `<a>`. Add a `?` to make it lazy: `<.*?>`. This single fact explains most patterns that "nearly work".

**Use a raw string for every pattern.** Write `r"\d+"`, not `"\d+"`. Without the `r`, Python processes the backslashes before `re` ever sees them, and the pattern you wrote is not the pattern that runs.

**A regular expression is the wrong tool for nested structure.** HTML, JSON and source code have a shape that patterns cannot follow reliably. Use a parser. Regular expressions are for flat text: a line, a field, a token.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. The `re` module is part of standard Python, so nothing needs installing.

A word on the prime-numbers project: it is a demonstration of how far pattern matching can be pushed, not advice. It is far slower than dividing, and it is on the page to show you something about how matching works, not to be used in a program.
