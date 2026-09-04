


# Script-Based Questions and Answers on Regular Expressions (`re`) in Python

## What this page contains, and why it matters

This page is a companion resource for Chapter 13 ("Regular Expressions") of the printed book *Python Programming: Problem Solving, Packages and Libraries*. It collects forty short, script-based questions — each one asking you to *write* a small Python program that demonstrates one particular idea about the [`re` module](https://docs.python.org/3/library/re.html) — grouped into **Part A: Questions Based Mainly on the Chapter Topics** (thirty questions, Q1–Q30) and **Part B: Advanced and Extension Questions** (ten questions, Q31–Q40).

Every script below has been run on Python 3.12.


If you would like the wider companion resources for this chapter, see [`10-ch13-re.md`](10-ch13-re.md) (eighteen worked example scripts, a primality-testing mini-project, a password validator, and a from-scratch regex engine), [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) (twenty-one short conceptual questions and answers), and [`60-ch13-re-capturing-noncapturing.md`](60-ch13-re-capturing-noncapturing.md) (a focused look at capturing versus non-capturing groups) in this same folder.

### A quick glossary (for reference while you read)

| Term | Plain-language meaning | Learn more |
|---|---|---|
| Regular expression (regex) | A text pattern that describes a *shape* of text to search for, rather than exact text | [Python `re` docs](https://docs.python.org/3/library/re.html) |
| Match object | The result Python gives you when a pattern is found in some text | [Python `re` — Match objects](https://docs.python.org/3/library/re.html#match-objects) |
| Capturing group | Part of a pattern wrapped in `( )` whose matched text can be pulled out separately with `.group(n)` | [Python `re` — groups](https://docs.python.org/3/library/re.html#re.Match.group) |
| Named group | A capturing group written `(?P<name>...)`, retrieved by name instead of number | [Python `re` — named groups](https://docs.python.org/3/library/re.html#index-17) |
| Backreference | Later in the *same* pattern, `\1` (or `(?P=name)`) means "match whatever group 1 already matched" | [Python `re` HOWTO — backreferences](https://docs.python.org/3/howto/regex.html) |
| Lookahead | `(?=...)`, a check that some text follows *without* actually consuming it as part of the match | [Python `re` HOWTO — lookahead assertions](https://docs.python.org/3/howto/regex.html#lookahead-assertions) |
| Greedy vs. lazy (non-greedy) | Whether a quantifier matches *as much text as possible* (greedy) or *as little as possible* (lazy, written with a trailing `?`) | [Python `re` HOWTO — greedy versus non-greedy](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy) |
| Quantifier | A symbol such as `*`, `+`, `?`, or `{m,n}` that says *how many times* something can repeat | [Python `re` HOWTO — repeating things](https://docs.python.org/3/howto/regex.html#repeating-things) |
| Catastrophic backtracking | A regex pattern that, on certain failing input, takes an *exponentially* long time to give up | [Python `re` HOWTO — backtracking notes](https://docs.python.org/3/howto/regex.html) |

### Table of contents

- [What this page contains, and why it matters](#what-this-page-contains-and-why-it-matters)
- [Part A: Questions based mainly on the chapter topics (Q1–Q30)](#part-a-questions-based-mainly-on-the-chapter-topics)
- [Part B: Advanced and extension questions (Q31–Q40)](#part-b-advanced-and-extension-questions)
- [Summary of changes made to this page](#summary-of-changes-made-to-this-page)

## Part A: Questions Based Mainly on the Chapter Topics

#### **Q1. Write a Python script using** `re.findall()` **to extract all digit sequences from a string. The script should show the difference between** `\d` **and** `\d+`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Sample string containing isolated and grouped digits
text = "My marks are 7, 89, and 1234."

# Step 3: \d matches ONE digit at a time, so every digit in the
# string is returned as its own separate match
single_digits = re.findall(r"\d", text)
print("Using \\d: ", single_digits)

# Step 4: \d+ matches one OR MORE consecutive digits, so a run of
# several digits next to each other is returned as one whole match
number_groups = re.findall(r"\d+", text)
print("Using \\d+:", number_groups)
```

```text
Using \d:  ['7', '8', '9', '1', '2', '3', '4']
Using \d+: ['7', '89', '1234']
```

**Explanation:**

- `\d` finds every individual digit separately, with no notion of "these digits belong together" — that is why `89` comes back as two separate matches, `'8'` and `'9'`.
- `\d+` combines consecutive digits into a single match instead, thanks to the `+` quantifier ("one or more"), which is why the same text produces the three whole numbers `'7'`, `'89'`, and `'1234'`.

>  **Extra practice question (not in the printed book):** What would `re.findall(r"\d*", text)` return instead of `\d+`? *(Try it yourself: `\d*` allows **zero** digits too, so — as with the very similar case in Q5 of [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) — you will see a number of extra empty-string matches `''` show up between the real numbers, one everywhere the pattern successfully matched "zero digits".)*

#### **Q2. Write a script that checks whether a string starts with the word** `Python` **using the** `^` **anchor.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Input string
text = "Python is powerful"

# Step 3: ^ anchors the match to the very START of the string, so
# "Python" only matches here if it is literally the first word
result = re.search(r"^Python", text)

# Step 4: Check whether the match succeeded, and report the result
if result:
    print("String starts with Python")
else:
    print("String does not start with Python")
```

```text
String starts with Python
```

**Explanation:**

- The caret `^` checks a *position* (the very beginning), not a character — it does not itself consume any of the text.
- Because `text` genuinely begins with the word "Python", `re.search()` succeeds and the first branch runs.

#### **Q3. Write a script that checks whether a string ends with** `.com` **using the** `$` **anchor.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Sample domain name
text = "example.com"

# Step 3: $ anchors the match to the very END of the string, so
# ".com" only matches here if it is literally the last four characters
result = re.search(r"\.com$", text)

# Step 4: Check whether the match succeeded, and report the result
if result:
    print("Valid .com domain")
else:
    print("Does not end with .com")
```

```text
Valid .com domain
```

**Explanation:**

- `\.` matches a literal full stop (an unescaped `.` would instead mean "any character," so the backslash is essential here).
- `$` ensures that `.com` appears at the very end of the string, not merely *somewhere* inside it.

#### **Q4. Write a script that extracts all lowercase letters from a string using the character class** `[a-z]`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with a deliberate mix of uppercase letters,
# lowercase letters, and digits
text = "PyThOn123abcXYZ"

# Step 3: [a-z] is a character class matching any single lowercase
# English letter -- digits and uppercase letters are simply skipped
lowercase_letters = re.findall(r"[a-z]", text)
print(lowercase_letters)
```

```text
['y', 'h', 'n', 'a', 'b', 'c']
```

**Explanation:**

- `[a-z]` represents any one lowercase English letter, from `a` through `z`.
- Each matching character is returned individually — `findall()` here is really just filtering the string down to its lowercase letters, one at a time.

#### **Q5. Write a script that extracts all non-digit characters from a string using** `\D`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text mixing letters and digits
text = "Room45A7"

# Step 3: \D matches anything that is NOT a digit -- the opposite
# of \d -- so digits are skipped and everything else is returned
result = re.findall(r"\D", text)
print(result)
```

```text
['R', 'o', 'o', 'm', 'A']
```

**Explanation:**

- Digits (`4`, `5`, `7`) are ignored entirely, since `\D` explicitly excludes them.
- Letters — and, in general text, symbols and spaces too — are matched instead, one character at a time.

#### **Q6. Write a script that replaces all whitespace characters in a string with a single dash (**`-`**). Use** `re.sub()`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with a deliberate mix of whitespace kinds:
# multiple spaces, a tab (\t), and a newline (\n)
text = "Python   is\tvery\nuseful"

# Step 3: \s+ matches ANY run of one or more whitespace characters
# (spaces, tabs, or newlines) in one go, and re.sub() replaces each
# such run with a single '-'
cleaned = re.sub(r"\s+", "-", text)
print(cleaned)
```

```text
Python-is-very-useful
```

**Explanation:**

- `\s` matches spaces, tabs, and newlines alike — it does not care which particular kind of whitespace it sees.
- The `+` quantifier combines an entire *run* of consecutive whitespace characters (however many, and of whatever mix) into a single match, which is why three spaces in a row still become just one dash, not three.

#### **Q7. Write a script that validates whether a PIN code contains exactly six digits.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a sample PIN
pin = "834001"

# Step 3: \d{6} means EXACTLY six digits, and fullmatch() additionally
# requires the ENTIRE string to satisfy the pattern -- not just some
# six-digit piece of a longer string
result = re.fullmatch(r"\d{6}", pin)

# Step 4: Report whether the PIN was valid
if result:
    print("Valid PIN")
else:
    print("Invalid PIN")
```

```text
Valid PIN
```



**Explanation:**

- `\d{6}` means *exactly* six digits — no more, no fewer (compare this to Q16's `{2,4}`-style ideas on [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) for other counted-repetition patterns).
- `re.fullmatch()` prevents *partial* matching: it insists the pattern account for the **entire** input string, not merely find a six-digit run somewhere inside a longer one. `re.search(r"\d{6}", "1834001")` would still find a match; `re.fullmatch()` would correctly reject it.

#### **Q8. Write a script that demonstrates the difference between** `re.match()` **and** `re.search()`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text where "Python" does NOT appear at the very start
text = "Welcome to Python programming"

# Step 3: match() checks ONLY at the beginning of the string. Since
# the text does not start with "Python", this fails and returns None
m1 = re.match(r"Python", text)

# Step 4: search() scans the ENTIRE string instead, so it finds
# "Python" wherever it happens to occur
m2 = re.search(r"Python", text)

print("re.match(): ", m1)
print("re.search():", m2)
```

```text
re.match():  None
re.search(): <re.Match object; span=(11, 17), match='Python'>
```

**Explanation:**

- `re.match()` fails here because "Python" is not the very first thing in the string — `text` begins with "Welcome", not "Python".
- `re.search()` succeeds because it scans the whole string looking for the pattern anywhere, and finds "Python" starting at index 11.
- This is exactly the same distinction explored in more depth under Q1 of [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md).

#### **Q9. Write a script that uses alternation (**`|`**) to search for either** `cat` **or** `dog` **in a sentence.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing "dog" but not "cat"
text = "I have a dog at home"

# Step 3: cat|dog means "match EITHER 'cat' OR 'dog'" -- the regex
# engine tries "cat" first at each position; if that fails, it tries
# "dog" before moving on
result = re.search(r"cat|dog", text)

# Step 4: Report whichever animal (if any) was found
if result:
    print("Animal found:", result.group())
else:
    print("No animal found")
```

```text
Animal found: dog
```

**Explanation:**

- The regex engine tries the alternatives left to right at each position in the string: "cat" fails everywhere in this text, so "dog" is tried and succeeds.
- The first alternative that actually succeeds is what gets returned — alternation does not try to find the "best" or "longest" alternative, only the first one that works.

#### **Q10. Write a script that uses grouping to repeat the word** `abc` **one or more times.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text made entirely of "abc" repeated three times
text = "abcabcabc"

# Step 3: (abc)+ groups the three letters "abc" together, so the '+'
# quantifier repeats the WHOLE group, not just the letter 'c'
result = re.fullmatch(r"(abc)+", text)
print(result)
```

```text
<re.Match object; span=(0, 9), match='abcabcabc'>
```

**Explanation:**

- Parentheses treat `abc` as one unit, so `+` means "one or more repeats of the whole three-letter sequence," not "one or more of just the last letter."
- `re.fullmatch()` confirms the entire nine-character string is accounted for by exactly three repeats of that unit.

#### **Q11. Write a script that extracts both username and domain name from an email address using capturing groups.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a sample email address
email = "student@gmail.com"

# Step 3: Two capturing groups -- (\w+) for the username before the
# '@', and (\w+\.\w+) for the domain after it
match = re.search(r"(\w+)@(\w+\.\w+)", email)

if match:
    print("Username:", match.group(1))
    print("Domain:  ", match.group(2))
```

```text
Username: student
Domain:   gmail.com
```

**Explanation:**

- Group 1, `(\w+)`, captures the username part of the email, everything before the `@`.
- Group 2, `(\w+\.\w+)`, captures the domain portion after the `@`, which itself consists of a word, a literal dot, and another word.

#### **Q12. Write a script that demonstrates the use of** `group()`**,** `start()`**,** `end()`**, and** `span()` **methods.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with a number embedded partway through
text = "Order number is 5678"

# Step 3: Find the run of digits in the text
match = re.search(r"\d+", text)

if match:
    print("Matched text:", match.group())
    print("Start index: ", match.start())
    print("End index:   ", match.end())
    print("Span:        ", match.span())
```

```text
Matched text: 5678
Start index:  16
End index:    20
Span:         (16, 20)
```

**Explanation:**

- `.group()` returns the actual matched text — here, the string `"5678"`.
- `.start()` and `.end()` return the character *positions* where the match begins and ends within the original string.
- `.span()` simply combines both of those into a single `(start, end)` tuple, which is often more convenient to pass around than the two numbers separately.

#### **Q13. Write a script that demonstrates partial consumption using** `re.match(r"\d+", text)`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with digits followed by other characters
text = "123 abc"

# Step 3: match() anchors at position 0. \d+ consumes only the
# digits -- it stops as soon as it reaches the space, since a space
# is not a digit
match = re.match(r"\d+", text)

if match:
    print("Matched:      ", match.group())
    print("Consumed span:", match.span())
    print("Remaining text:", text[match.end():])
```

```text
Matched:       123
Consumed span: (0, 3)
Remaining text:  abc
```

**Explanation:**

- Only the digits `"123"` are consumed by the match — `\d+` has no way to match the space or the letters that follow, so it simply stops there.
- The remaining characters (`" abc"`, including the leading space) are left completely untouched, and can be retrieved with ordinary string slicing from `match.end()` onward.

#### **Q14. Write a script that demonstrates full consumption of a string using** `.*`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up the same text as Q13, for direct comparison
text = "123 abc"

# Step 3: \d+.* first consumes the digits, and then .* greedily
# consumes EVERYTHING else that follows, right to the end of the string
match = re.match(r"\d+.*", text)

if match:
    print("Entire consumed text:", match.group())
    print("Span:                ", match.span())
```

```text
Entire consumed text: 123 abc
Span:                 (0, 7)
```

**Explanation:**

- `.*` consumes all of the remaining characters after the digits — the space and the letters `"abc"` alike — because `.` matches almost any character and `*` allows any number of repeats, including "as many as there are left."
- Compare this directly with Q13: swapping a bare `\d+` for `\d+.*` is the difference between consuming *only* the digits and consuming the *entire rest of the string* — the whole match now spans all seven characters, `(0, 7)`, instead of stopping at `(0, 3)`.

#### **Q15. Write a script that extracts all words from a sentence using** `\w+`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a short sentence ending with punctuation
text = "Python is fun!"

# Step 3: \w+ matches runs of "word characters" -- letters, digits,
# and underscores -- so punctuation like '!' is naturally excluded
words = re.findall(r"\w+", text)
print(words)
```

```text
['Python', 'is', 'fun']
```

**Explanation:**

- `\w` matches letters, digits, and the underscore character — but *not* punctuation, spaces, or most other symbols.
- The `+` quantifier groups consecutive word characters together into whole words, which is exactly why "Python", "is", and "fun" each come back as one single match rather than being split letter by letter (compare this with Q4's `[a-z]`, which deliberately matches only *one* character at a time).

#### **Q16. Write a script that splits a sentence into words using** `re.split()`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with THREE different kinds of separator: a
# comma, a semicolon, and a space
text = "Apple,Orange;Banana Grape"

# Step 3: [,;\s]+ is a character class matching a comma, a semicolon,
# OR any whitespace character -- the '+' lets one or more of these,
# in any mixture, count as a single separator
parts = re.split(r"[,;\s]+", text)
print(parts)
```

```text
['Apple', 'Orange', 'Banana', 'Grape']
```

**Explanation:**

- The character class `[,;\s]` contains every kind of separator this text might use, all treated as equally valid split points.
- The `+` quantifier combines consecutive separators together, which matters here because "Banana Grape" is separated by a plain space while the other words use punctuation — `re.split()` handles all three separator styles uniformly in one call, which plain [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split) could not do without several separate calls.

#### **Q17. Write a script that demonstrates the difference between greedy and non-greedy matching.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing TWO separate pairs of <b>...</b> tags
text = "<b>Python</b><b>Java</b>"

# Step 3: Greedy match. .* tries to match as MUCH text as possible,
# so it stretches from the very FIRST '<b>' all the way to the very
# LAST '</b>' in the string, swallowing the second tag pair whole
greedy = re.findall(r"<b>.*</b>", text)
print("Greedy:    ", greedy)

# Step 4: Non-greedy match. .*? tries to match as LITTLE text as
# possible, so it stops at the FIRST '</b>' it can reach -- giving
# two separate, correctly-paired matches instead of one big one
nongreedy = re.findall(r"<b>.*?</b>", text)
print("Non-greedy:", nongreedy)
```

```text
Greedy:     ['<b>Python</b><b>Java</b>']
Non-greedy: ['<b>Python</b>', '<b>Java</b>']
```



**Explanation:**

- `.*` (greedy) grabs the maximum possible text between the first `<b>` and the last `</b>` in the whole string — including the second `<b>Java</b>` pair sitting right in the middle of that span — which is almost never what you actually want when matching tag-like structures.
- `.*?` (non-greedy, marked by the trailing `?`) grabs the minimum possible text instead, stopping at the very first `</b>` it reaches, which correctly separates the two tag pairs. This is the same greedy-vs-lazy idea explored on [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) (Q10) and used throughout [`10-ch13-re.md`](10-ch13-re.md).

#### **Q18. Write a script that counts how many replacements were made using** `re.subn()`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing three separate numbers
text = "Marks: 45, 67, 89"

# Step 3: subn() behaves like sub(), but ALSO returns a count of how
# many replacements it made, as the second item of a tuple
result = re.subn(r"\d+", "#", text)
print(result)
```

```text
('Marks: #, #, #', 3)
```

**Explanation:**

- `re.subn()` returns a **tuple** of two items, unlike plain `re.sub()`, which returns only the modified string.
- The first item is the modified string itself; the second item is a count of how many replacements were actually made — here, `3`, one for each number found.

#### **Q19. Write a script that uses named groups to extract a date in the format** `DD-MM-YYYY`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing a date
text = "Today's date is 08-05-2026"

# Step 3: (?P<name>...) creates a NAMED capturing group -- functionally
# identical to an ordinary numbered group, but retrieved by a readable
# name instead of a bare number
pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"
match = re.search(pattern, text)

if match:
    print(match.groupdict())
```

```text
{'day': '08', 'month': '05', 'year': '2026'}
```

**Explanation:**

- Named groups let you build a dictionary-like result via `.groupdict()`, rather than having to remember that "group 1 is the day, group 2 is the month," and so on.
- The dictionary's keys come directly from the names chosen in the pattern (`day`, `month`, `year`), which makes the code that reads the result much easier to follow than `match.group(1)`, `match.group(2)`, `match.group(3)` would be.

#### **Q20. Write a script that uses** `re.escape()` **to safely search for the literal text** `a+b`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing a literal plus sign
text = "a+b"

# Step 3: re.escape() automatically backslash-escapes every special
# regex character in a plain string, so the result matches that
# EXACT text literally, rather than treating '+' as a quantifier
safe_pattern = re.escape("a+b")
result = re.fullmatch(safe_pattern, text)
print(result)
```

```text
<re.Match object; span=(0, 3), match='a+b'>
```

**Explanation:**

- Normally, `+` means "one or more of the preceding thing" in a regex — it does *not* mean a literal plus sign.
- `re.escape()` removes this special meaning by inserting a backslash before it (and before any other special character in the string), which is exactly what you want when building a pattern out of text that might contain regex metacharacters you did not choose yourself — see also Q7 of [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) for another worked example of `re.escape()`.

#### **Q21. Write a script that demonstrates the use of a compiled Pattern object.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Compile the pattern ONCE, up front
pattern = re.compile(r"\d+")

# Step 3: Reuse the SAME compiled Pattern object against two
# different pieces of text, instead of recompiling the pattern
# from scratch each time
text1 = "123"
text2 = "456"
print(pattern.match(text1))
print(pattern.match(text2))
```

```text
<re.Match object; span=(0, 3), match='123'>
<re.Match object; span=(0, 3), match='456'>
```

**Explanation:**

- Compiled patterns are reusable — the pattern object `pattern` is built once, and then its methods (`.match()`, `.search()`, `.findall()`, and so on) can be called repeatedly against as many different strings as needed.
- This is especially useful for repeated matching, since Python does not need to re-parse the same pattern text over and over — see Q21 of [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md), which measures the actual timing benefit of this.

#### **Q22. Write a script that prints the attributes** `pattern`**,** `groups`**, and** `groupindex` **of a compiled Pattern object.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Compile a pattern with one named group and one unnamed
# (numbered-only) group
pattern = re.compile(r"(?P<word>\w+)-(\d+)")

# Step 3: Printing the Pattern object itself shows Python's own
# repr() of it -- note the DOUBLE backslashes, since this is how
# Python represents a string that itself contains a backslash
print("Pattern:      ", pattern)

# Step 4: The .pattern attribute instead gives back the ORIGINAL
# pattern text as a plain string, with single backslashes as typed
print("Pattern text: ", pattern.pattern)

# Step 5: .groups is the total COUNT of capturing groups in the
# pattern (named groups count too)
print("Group count:  ", pattern.groups)

# Step 6: .groupindex maps each named group's name to its group
# NUMBER -- here, "word" is group 1
print("Named groups: ", pattern.groupindex)
```

```text
Pattern:       re.compile('(?P<word>\\w+)-(\\d+)')
Pattern text:  (?P<word>\w+)-(\d+)
Group count:   2
Named groups:  {'word': 1}
```

**Explanation:**

- `pattern` (printing the object itself) shows Python's `repr()` of the compiled pattern, which is why the backslashes appear doubled — that is simply how Python displays a string containing a literal backslash, not a difference in the pattern's actual behaviour.
- `pattern.pattern` gives back the *original* regex text as a plain, readable string — useful for logging or debugging.
- `pattern.groups` is the total number of capturing groups (here, `2`: the named group `word` and the unnamed group for the digits).
- `pattern.groupindex` is a dictionary mapping every *named* group to its group number — here, `{'word': 1}`, since `word` happens to be the first (and only named) group in this pattern.

#### **Q23. Write a script that validates whether a password contains at least one digit and one uppercase letter.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a candidate password
password = "Python123"

# Step 3: Build the pattern out of two POSITIVE LOOKAHEADS plus a
# minimum-length check:
#   (?=.*[A-Z])  -- somewhere ahead, there must be an uppercase letter
#   (?=.*\d)     -- somewhere ahead, there must be a digit
#   .{8,}        -- the string itself must be at least 8 characters
# Lookaheads CHECK for something without consuming any characters,
# so both can "look" at the very same text independently
pattern = r"(?=.*[A-Z])(?=.*\d).{8,}"
result = re.fullmatch(pattern, password)

if result:
    print("Strong password")
else:
    print("Weak password")
```

```text
Strong password
```

**Explanation:**

- `(?=.*[A-Z])` checks that an uppercase letter exists *somewhere* in the string, without actually consuming any of it — this is what makes a lookahead different from an ordinary pattern piece.
- `(?=.*\d)` performs the same kind of check for a digit.
- `.{8,}` ensures the whole password is at least 8 characters long. Because `"Python123"` has an uppercase `P`, several digits, and is 9 characters long, all three conditions are satisfied and `re.fullmatch()` succeeds.

>  **Extra practice question (not in the printed book):** the fuller password-validation walkthrough on [`10-ch13-re.md`](10-ch13-re.md) checks for lowercase letters and special characters too, using several lookaheads chained together in exactly this style — worth comparing against this shorter, two-condition version here.

#### **Q24. Write a script that extracts all words beginning with a capital letter.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a sentence where every word happens to start with
# a capital letter
text = "Python and Java are Programming Languages"

# Step 3: \b[A-Z]\w* means: start at a word boundary, require the
# FIRST character to be uppercase, then allow any number of further
# word characters (which may be upper OR lower case) to follow
result = re.findall(r"\b[A-Z]\w*", text)
print(result)
```

```text
['Python', 'Java', 'Programming', 'Languages']
```

**Explanation:**

- `\b` (word boundary) ensures the match starts exactly at the beginning of a word, not partway through one.
- `[A-Z]` checks that this very first letter is uppercase.
- `\w*` then allows any number of *additional* word characters (letters, digits, or underscore, in either case) to follow, so the rest of a longer word like "Programming" is captured along with its capital first letter. Notice that "and" and "are" are correctly excluded, since they begin with lowercase letters.

#### **Q25. Write a script that finds all repeated vowels in a string using quantifiers.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with runs of repeated vowels
text = "cooool beeaautiful"

# Step 3: [aeiou]{2,} means "two or more vowels IN A ROW" -- a
# single, isolated vowel does NOT count, only genuine repeats/runs
result = re.findall(r"[aeiou]{2,}", text)
print(result)
```

```text
['oooo', 'eeaau']
```

> **Fix applied here:** the original comment claimed this would print `['ooo', 'eeaa', 'uu']` — three separate matches. Counting the vowels carefully in `"cooool beeaautiful"` shows this is not correct: `"cooool"` contains **four** consecutive `o`s (`c-o-o-o-o-l`), not three, and in `"beeaautiful"` the run `e-e-a-a-u` is **one single, unbroken** run of five vowels (`"eeaau"`) — it is not split into a separate `"eeaa"` and `"uu"`, because there is no non-vowel character sitting between the `a` and the `u`. The corrected, verified output is `['oooo', 'eeaau']` — two matches, not three.

**Explanation:**

- `{2,}` means "two or more repetitions" of whatever comes immediately before it — here, the character class `[aeiou]`.
- The character class limits the search to vowels only, but once a run of two or more vowels is found, the *entire unbroken run* becomes a single match — this is exactly why `"eeaau"` (five vowels with no consonant in between) comes back as one match rather than being artificially split.

#### **Q26. Write a script that extracts all hexadecimal numbers from a string.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing two hex colour codes
text = "Colors: #FFAA00 and #12BC9A"

# Step 3: '#' matches the literal hash symbol, [A-Fa-f0-9] matches
# any single hexadecimal digit (case-insensitive), and {6} requires
# EXACTLY six of them
result = re.findall(r"#[A-Fa-f0-9]{6}", text)
print(result)
```

```text
['#FFAA00', '#12BC9A']
```

**Explanation:**

- Hexadecimal digits are `0`-`9` plus `A`-`F` (or `a`-`f`) — the character class `[A-Fa-f0-9]` covers both letter cases explicitly, since regex character classes are case-sensitive by default.
- `{6}` ensures exactly six hex digits follow the `#`, matching the standard six-digit colour-code format used in HTML and CSS.

#### **Q27. Write a script that checks whether a string contains only alphabets and spaces.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing only letters and spaces
text = "Python Programming"

# Step 3: [A-Za-z ]+ matches one or more characters, each of which
# must be an uppercase letter, a lowercase letter, or a literal space
# -- fullmatch() then requires the ENTIRE string to be made of these
result = re.fullmatch(r"[A-Za-z ]+", text)

if result:
    print("Valid text")
else:
    print("Contains invalid characters")
```

```text
Valid text
```

**Explanation:**

- The character class `[A-Za-z ]` includes uppercase letters, lowercase letters, and the space character itself (placed plainly inside the brackets).
- `+` ensures at least one character is present, and `re.fullmatch()` insists every single character in the string belongs to that set — a string containing so much as one digit or punctuation mark would fail this check.

#### **Q28. Write a script that extracts all hashtags from a social media post.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing two hashtags
text = "Learning #Python and #Regex is fun"

# Step 3: #\w+ matches a literal '#' immediately followed by one or
# more word characters -- this naturally stops at the first space
# or punctuation mark after the hashtag word
hashtags = re.findall(r"#\w+", text)
print(hashtags)
```

```text
['#Python', '#Regex']
```

**Explanation:**

- `#` matches the literal hashtag symbol itself.
- `\w+` then captures the hashtag's text — letters, digits, and underscores — stopping naturally as soon as it reaches a space or any other non-word character.

#### **Q29. Write a script that demonstrates** `re.finditer()` **by printing all matches and their positions.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a short sentence of three words
text = "cat bat rat"

# Step 3: finditer() returns an ITERATOR of Match objects, one per
# match, produced one at a time rather than as one big list up front
for match in re.finditer(r"\w+", text):
    print("Word:    ", match.group())
    print("Position:", match.start(), match.end())
```

```text
Word:     cat
Position: 0 3
Word:     bat
Position: 4 7
Word:     rat
Position: 8 11
```

**Explanation:**

- Each iteration of the loop produces one full `Match` object — not just the matched text, but also its position and (if the pattern had any) its groups.
- Position information is available on every match via `.start()` and `.end()`, which is exactly what makes `finditer()` more powerful than `findall()` whenever you need to know *where* each match occurred, not just *what* it was — see also Q14 of [`50-ch13-re-conceptual-qa.md`](50-ch13-re-conceptual-qa.md) for a comparison of `search()`, `findall()`, and `finditer()` side by side.

#### **Q30. Write a script that extracts only the file extensions from filenames.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text listing three different filenames
text = "report.pdf image.png notes.txt"

# Step 3: \. matches a literal dot, and the CAPTURING group
# ([A-Za-z0-9]+) grabs the extension text that follows it --
# findall() then returns only what the group captured, not the
# whole "filename.ext" match
extensions = re.findall(r"\.([A-Za-z0-9]+)", text)
print(extensions)
```

```text
['pdf', 'png', 'txt']
```

**Explanation:**

- `\.` matches the literal dot separating a filename from its extension.
- Because the extension part is wrapped in parentheses — a capturing group — `findall()` returns *only* the captured extension text for each match, not the dot itself and not the filename that came before it. This is the same "capture only the piece you want" technique explored in much more depth on [`60-ch13-re-capturing-noncapturing.md`](60-ch13-re-capturing-noncapturing.md).

## Part B: Advanced and Extension Questions

#### **Q31. Write a script that validates IPv4 addresses using Regular Expressions.**

**Answer:**

An IPv4 address is four numbers ("octets"), each between 0 and 255, separated by dots — for example `192.168.1.1`. The tricky part is that a plain `\d{1,3}` for each octet would also happily accept nonsense like `999`, so the pattern below spells out the valid ranges explicitly.

| Piece of the octet pattern | Matches | Why |
|---|---|---|
| `25[0-5]` | 250–255 | `25` followed by a digit no higher than `5` |
| `2[0-4]\d` | 200–249 | `2` followed by a digit `0`–`4`, then any digit |
| `1\d\d` | 100–199 | `1` followed by any two digits |
| `[1-9]?\d` | 0–99 | an optional leading digit `1`–`9`, then any digit (this also covers single digits `0`–`9`) |

```python
# Step 1: Import re
import re

# Step 2: Set up a valid sample IP address
ip = "192.168.1.1"

# Step 3: Build ONE octet pattern covering all valid values 0-255,
# by combining the four ranges from the table above with alternation
octet = r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"

# Step 4: A full IPv4 address is one octet, followed by exactly THREE
# more ".octet" groups, anchored at both ends so the WHOLE string
# must match -- not just some substring of it
pattern = r"^" + octet + r"(\." + octet + r"){3}$"

result = re.fullmatch(pattern, ip)

if result:
    print("Valid IP")
else:
    print("Invalid IP")
```

```text
Valid IP
```

**Explanation:**

- `^` and `$` ensure the *entire* string matches the pattern, not just some IP-shaped piece buried inside a longer string.
- Each octet must independently fall in the 0–255 range, using the four alternatives from the table above; the `\.` between them matches the literal dots separating the four numbers.

>  **Extra practice question (not in the printed book):** try the same pattern against `"256.1.1.1"`, `"999.999.999.999"`, and `"1.2.3"` (too few octets). All three correctly come back as **invalid** — `256` and `999` do not fit any of the four range alternatives, and `"1.2.3"` has only three octets instead of the required four. Try it yourself, or see [`10-ch13-re.md`](10-ch13-re.md) for further worked validation examples in this style.

#### **Q32. Write a script that masks credit card numbers except the last four digits.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up sample text containing a 16-digit card number
text = "My card number is 1234567812345678"

# Step 3: \d(?=\d{4}) matches any SINGLE digit that has EXACTLY four
# more digits somewhere immediately after it. (?=\d{4}) is a positive
# lookahead: it CHECKS for four digits ahead without consuming them,
# so those four digits remain available for the next \d(?=\d{4})
# check (and are never themselves matched/replaced)
masked = re.sub(r"\d(?=\d{4})", "*", text)
print(masked)
```

```text
My card number is ************5678
```

**Explanation:**

- `(?=\d{4})` is a positive lookahead — it requires four digits to follow at this position, but does **not** consume them as part of the match, so they stay in the string unchanged for the next check to see.
- Because every digit *except* the last four has "four more digits after it" somewhere down the line, every digit except the final four gets matched (and replaced with `*`) by this pattern, one at a time, from left to right.

#### **Q33. Write a script that removes duplicate consecutive words from a sentence.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with two different duplicated words
text = "This is is a test test sentence"

# Step 3: \b(\w+)\s+\1\b finds a word, captured in group 1, followed
# by whitespace and then the SAME word again (the backreference \1).
# The replacement r"\1" keeps just ONE copy of the word
cleaned = re.sub(r"\b(\w+)\s+\1\b", r"\1", text)
print(cleaned)
```

```text
This is a test sentence
```

**Explanation:**

- `(\w+)` captures a word, and `\1` immediately afterward insists on seeing that *exact same* word again, right after some whitespace.
- The trailing `\b` (word boundary) ensures the repeated match is a whole word, not merely a matching prefix of a longer, different word.
- This is a smaller, single-pass version of the same idea explored in much more depth (including a version that removes runs of *three or more* repeats, and a `finditer()`-based reporting script) under [Case study: removing duplicate words with a backreference](60-ch13-re-capturing-noncapturing.md#case-study-removing-duplicate-words-with-a-backreference) on `60-ch13-re-capturing-noncapturing.md`.

#### **Q34. Write a script that extracts all HTML tag names from a string.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a small, well-formed piece of HTML
html = "<html><body><h1>Title</h1></body></html>"

# Step 3: <\/?([a-zA-Z0-9]+) matches an opening OR a closing tag --
# '<' followed by an OPTIONAL '/' (for closing tags), then captures
# just the tag NAME that follows, stopping before the closing '>'
result = re.findall(r"<\/?([a-zA-Z0-9]+)", html)
print(result)
```

```text
['html', 'body', 'h1', 'h1', 'body', 'html']
```

**Explanation:**

- `\/?` makes the forward slash optional, so the same pattern matches both an opening tag like `<html>` and its closing counterpart `</html>` — the `?` after `\/` means "zero or one of these."
- The capturing group `([a-zA-Z0-9]+)` grabs just the tag *name* itself (`html`, `body`, `h1`), not the surrounding angle brackets or slash, which is why `findall()` returns six tag names — three opening, three closing — rather than six full tag strings like `<html>`.

#### **Q35. Write a script that converts dates from** `DD/MM/YYYY` **format to** `YYYY-MM-DD` **format using** `re.sub()`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing a date in DD/MM/YYYY format
text = "Today's date is 08/05/2026"

# Step 3: Three capturing groups pick out day, month, and year
# separately; the replacement string \3-\2-\1 then REARRANGES them
# into year-month-day order, joined by dashes instead of slashes
new_text = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)
print(new_text)
```

```text
Today's date is 2026-05-08
```

**Explanation:**

- `(\d{2})` captures the day, `(\d{2})` captures the month, and `(\d{4})` captures the year — three separate groups, numbered 1 through 3 in the order their *opening* parentheses appear.
- The replacement string `r"\3-\2-\1"` does not have to use the groups in their original order — it deliberately rearranges them (year first, then month, then day) to build the new date format, which is exactly what makes backreferences in a replacement string so useful for reformatting structured text like dates.

#### **Q36. Write a script that tokenizes a sentence into words and punctuation marks separately.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up a sentence containing three punctuation marks
text = "Hello, world! How are you?"

# Step 3: \w+|[^\w\s] is an ALTERNATION between two very different
# things: \w+ matches a whole word, while [^\w\s] matches a SINGLE
# character that is neither a word character NOR whitespace (i.e.
# punctuation). Together, every word and every punctuation mark
# becomes its own separate token, and plain whitespace is skipped
tokens = re.findall(r"\w+|[^\w\s]", text)
print(tokens)
```

```text
['Hello', ',', 'world', '!', 'How', 'are', 'you', '?']
```

**Explanation:**

- Alternation (`|`) lets one pattern describe two very different kinds of token — whole words on one side, single punctuation characters on the other — and `findall()` collects every match of *either* kind, in the order they appear.
- This kind of word-and-punctuation splitting is a first, simple step towards **tokenization**, a standard early stage in Natural Language Processing pipelines.

#### **Q37. Write a script that identifies repeated whitespace in a text file and compresses it into single spaces.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text with several DIFFERENT kinds of whitespace
# bunched together: multiple spaces, two tabs, and two newlines
text = "Python    is\t\tvery\n\nuseful"

# Step 3: \s+ matches ANY run of one or more whitespace characters
# -- regardless of whether that run is made of spaces, tabs,
# newlines, or a mixture of all three -- and replaces the whole run
# with exactly one space
cleaned = re.sub(r"\s+", " ", text)
print(cleaned)
```

```text
Python is very useful
```

**Explanation:**

- `\s+` matches a run of one or more whitespace characters of *any* kind — this single pattern handles the multiple spaces, the double tab, and the double newline all uniformly, without needing separate rules for each.
- This is the same underlying idea as Q6 above (replacing whitespace with a dash), applied here to *normalise* messy whitespace down to single spaces instead of replacing it with a visible separator — a common cleanup step when processing text pasted from elsewhere.

#### **Q38. Write a script that extracts URLs beginning with either** `http` **or** `https`**.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Set up text containing one https:// URL and one http:// URL
text = "Visit https://python.org and http://example.com"

# Step 3: https?://\S+ breaks down as: 'http', an OPTIONAL 's'
# (matching both http and https), then '://', then \S+ to grab
# everything else up to the next whitespace
urls = re.findall(r"https?://\S+", text)
print(urls)
```

```text
['https://python.org', 'http://example.com']
```

**Explanation:**

- `s?` makes the letter `s` optional, which is exactly what lets one single pattern match both `http://` and `https://` URLs without needing two separate patterns joined by alternation.
- `\S+` (any non-whitespace character, one or more times) captures the rest of each URL — the domain and any path — stopping naturally at the next space in the sentence.

#### **Q39. Write a script that demonstrates catastrophic backtracking using a badly designed regex and explain why it is dangerous.**

**Answer:**

```python
# Step 1: Import re and time (to measure how long matching takes)
import re
import time

# Step 2: A DELIBERATELY poorly designed pattern: (a+)+ nests one
# quantified group INSIDE another quantified group. There are many
# different ways to split a run of 'a's between the inner and outer
# '+', and the regex engine will try almost all of them before
# giving up on a failing match
pattern = r"(a+)+$"

# Step 3: Build a string of 25 'a's followed by 'X' -- a character
# that can never satisfy the pattern, forcing the engine to
# exhaustively try every possible way of grouping the 'a's before
# it can be sure no arrangement works
text = "a" * 25 + "X"

# Step 4: Time how long the (failing) match takes
start = time.time()
result = re.match(pattern, text)
end = time.time()

print("Match:      ", result)
print("Time taken: ", round(end - start, 4), "seconds")
```

```text
Match:       None
Time taken:  1.3281 seconds
```

*(Your own timing will vary depending on your machine, but it will be dramatically slower than every other script on this page — most of which complete in a small fraction of a millisecond.)*

**Explanation:**

- Nested quantifiers like `(a+)+` can trigger **excessive backtracking**, because the regex engine has many different ways to divide the same run of `a`s between the *inner* `+` (repeats within one group) and the *outer* `+` (repeats of the whole group) — and when the overall match ultimately fails, it has to try essentially all of them before giving up.
- The table below shows just how quickly this gets out of hand as the string grows by only a few characters at a time — this is measured, real timing data, re-run while preparing this page:

| Number of `a`s before the failing `X` | Time taken |
|---|---|
| 10 | 0.0001 s |
| 15 | 0.0014 s |
| 18 | 0.0105 s |
| 20 | 0.0426 s |
| 22 | 0.1716 s |
| 24 | 0.6785 s |
| 25 | 1.3281 s |

Notice the pattern: each time the string grows by just one or two characters, the time taken roughly **doubles or quadruples**. This is the signature of *exponential* time complexity — a 30-character string here would likely take minutes, and a 40-character one could take longer than you would ever wait, all from a pattern that looks harmless at a glance. This is exactly why catastrophic backtracking is **dangerous in performance-sensitive systems**: an attacker (or simply an unlucky user) who can control the input to a vulnerable regex can cause your program to hang indefinitely, a class of security issue known as **ReDoS** (Regular Expression Denial of Service).

#### **Q40. Write a script that builds a mini regex tester where the user enters a pattern and a test string, and the script reports whether a match exists.**

**Answer:**

```python
# Step 1: Import re
import re

# Step 2: Ask the user for a pattern and a piece of text to test it
# against
pattern = input("Enter regex pattern: ")
text = input("Enter test string: ")

# Step 3: Wrap the search in try/except, since a user-typed pattern
# might not be VALID regex syntax at all (e.g. an unmatched
# parenthesis) -- re.error is the exception Python raises in that case
try:
    result = re.search(pattern, text)
    if result:
        print("Match found:", result.group())
        print("Span:       ", result.span())
    else:
        print("No match found")
except re.error as e:
    print("Invalid regex pattern:", e)
```

Since this script waits for the user to type input, it has no single fixed output — instead, here are two example runs captured while testing it:

```text
Enter regex pattern: \d+
Enter test string: Room 42B
Match found: 42
Span:        (5, 7)
```

```text
Enter regex pattern: (unclosed
Enter test string: anything
Invalid regex pattern: missing ), unterminated subpattern at position 0
```

**Explanation:**

- This script allows hands-on experimentation with regex — you can type any pattern and any text and immediately see whether, and where, it matches, which makes it a genuinely useful tool for checking your own patterns while working through the other 39 questions on this page.
- The `try`/`except re.error` block handles invalid patterns safely: without it, typing a broken pattern like `"(unclosed"` (a parenthesis with no matching close) would crash the whole script with an unhandled exception instead of reporting a friendly error message.
- This is a small but genuinely useful educational mini-project — the same core idea used by many "regex playground" websites, just running locally in your own terminal.

