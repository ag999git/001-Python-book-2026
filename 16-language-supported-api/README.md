
# Chapter 16: Python Libraries for Data Structures and Algorithms

The online companion to Chapter 16 of the book. The printed chapter introduces the parts of the Python Standard Library that handle data structures and algorithms. These pages carry the worked exercises, the real-world examples, and the full answers to every question at the end of the chapter.

By the end of these pages you should know which ready-made structure to reach for in a given situation, be able to reason about how long an algorithm will take as the data grows, and have written each of the classic searching and sorting algorithms yourself.

You need to be comfortable with lists, dictionaries, loops and functions before starting.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Converting a NamedTuple into a Dictionary](010-ch16-namedtuple2dict.md) | A worked exercise: building a record with `namedtuple`, turning it into a dictionary with `zip()`, and the `_asdict()` shortcut that does it for you | Start here |
| [Real-World Python: Practical Uses for Standard Library Modules](020-ch16-real-world-use.md) | `collections`, `heapq`, `bisect`, `queue`, `enum`, `dataclasses` and `functools`, each shown solving a problem you would actually meet | The heart of the chapter |
| [Conceptual Questions with Answers](060-ch16-conceptual-qa.md) | Big-O notation explained from scratch, then full answers to the conceptual questions printed in the book | Revision |
| [Scripting Questions with Answers](065-ch16-scripting-qa-easy.md) | Twenty short programs with complete answers: linear and binary search, bubble, insertion and selection sort, stacks, queues and the `collections` types | Practice |
| [Advanced Scripting Questions with Answers](070-ch16-scripting-qa-hard.md) | Twenty harder programs: timing comparisons, early-exit sorting, producer-consumer threads, an LRU cache, `groupby` and measured Big-O growth | Practice, after the easier set |

## Suggested Reading Order

1. **Converting a NamedTuple into a Dictionary** as a gentle start; it is one exercise, worked through completely.
2. **Real-World Python** for the modules themselves. Read it module by module rather than in one sitting.
3. **Conceptual Questions** to check that the ideas have stuck, particularly Big-O.
4. **Scripting Questions** to write the algorithms yourself.
5. **Advanced Scripting Questions** last. These assume everything above.

A word on the two scripting pages: try each question before reading its answer. The answers are complete working programs, which makes them easy to read and easy to learn nothing from.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Each answer shows the output it produces, so you can compare. A few of the timing scripts print different numbers on different machines, which is expected and is explained where it happens.


