# Chapter 19: Tuples, Dictionaries and Sets

The online companion to Chapter 19 of the book. The printed chapter introduces Python's other three built-in collections. These pages carry the full answers to all one hundred and twenty questions at the end of the chapter, twenty conceptual and twenty scripting for each of the three types.

By the end of these pages you should know when a tuple is the right choice and when a list is, what makes an object usable as a dictionary key, how a dictionary finds a value without searching, and why a set answers "have I seen this before?" thousands of times faster than a list.

You need Chapter 18 (Lists) first. Nothing else is assumed.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Tuples: Conceptual Questions and Answers](50-ch19-tuples-conceptual-qa.md) | Twenty questions in eight parts, from the trailing comma to nested tuples | Start here |
| [Tuples: Scripting Questions and Answers](70-ch19-tuples-scripting-qa.md) | Twenty worked programs on the same ground | After the conceptual page |
| [Dictionaries: Conceptual Questions and Answers](80-ch19-dictionary-conceptual-qa.md) | Twenty questions in six parts, including how hashing actually works | The heart of the chapter |
| [Dictionaries: Scripting Questions and Answers](90-ch19-dictionary-scripting-qa.md) | Twenty worked programs: counting, grouping, merging, copying | Practice |
| [Sets: Conceptual Questions and Answers](95-ch19-sets-conceptual-qa.md) | Twenty questions in six parts, from uniqueness to `frozenset` | After dictionaries |
| [Sets: Scripting Questions and Answers](98-ch19-sets-scripting-qa.md) | Twenty worked programs on duplicates, membership and set operations | Practice |

## How the Pages Are Organised

Each of the three types has the same pair of pages: a conceptual one that explains why Python behaves as it does, and a scripting one with twenty complete programs. Every page opens with a table of key terms and closes with a quick revision summary.

| Type | Conceptual parts | Scripting parts |
| --- | --- | --- |
| Tuples | Creating and writing; immutability and slicing; performance against lists; packing and unpacking; converting and sorting; tuples as dictionary keys; everyday uses; nested tuples | Creating; reading and joining; slicing; unpacking; testing; swapping and keys; sorting and nesting; functions, loops and `match-case` |
| Dictionaries | What a dictionary is; keys and hashing; creating; traversing; view objects; operators and methods | Creating and reading; looping; comprehensions and valid keys; checking, merging, removing, grouping; copies and views; counting, pairing, comparing |
| Sets | What a set is; creating and inspecting; hashability; compared with lists and dictionaries; speed and set operations; the unchangeable set | Creating and removing duplicates; what a set can hold; adding and removing; speed and safe changes; set operations; choosing the right structure |

## Suggested Reading Order

1. **Tuples, conceptual then scripting.** Tuples are the simplest of the three, and the immutability rule explains nearly all of their behaviour.
2. **Dictionaries, conceptual first.** Part 2, on keys and hashing, is the most valuable section in the chapter. It explains why keys must be immutable, why lookup is fast whatever the size, and what a "collision" is.
3. **Dictionaries, scripting.** These are the patterns you will reuse most: counting with `get()`, grouping with `setdefault()`, merging with `update()`.
4. **Sets last.** Once hashing makes sense, sets are easy: a set is a dictionary with the values thrown away.

## Four Points Worth Extra Care

**A single value in brackets is not a tuple.** `x = (5)` gives an integer. It is the comma that makes a tuple, not the brackets: `x = (5,)`.

**A key must be hashable, and a tuple is hashable only if everything inside it is.** `(1, 2)` works as a key. `(1, [2, 3])` does not, because of the list inside.

**Never change a dictionary or a set while looping over it.** Python raises `RuntimeError: dictionary changed size during iteration`. Loop over a snapshot instead, such as `list(my_dict)`.

**`d[key]` and `d.get(key)` behave differently when the key is missing.** The first raises `KeyError` and stops the program; the second returns `None`, or whatever default you give it.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Every output shown was produced by running the script above it.

Three kinds of output will differ on your machine, and that is expected. Any script that prints `id()` or `hash()` shows numbers your computer chooses. Any script that times two approaches shows speeds that depend on your hardware; only the size of the difference is meant to match. And because a set has no order, the items may print in a different order from the page.

