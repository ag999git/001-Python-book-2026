
# Chapter 9: Exceptions

The online companion to Chapter 9 of the book. The printed chapter covers `try`, `except`, `else` and `finally`, the exception hierarchy, and raising your own. These pages carry a bank of conceptual questions, forty script exercises, and four pages on the topics the chapter opens but has no room to finish: context managers, reading a traceback, and fetching data from the internet, where things go wrong for real.

By the end of these pages you should be able to catch the right exception rather than a bare `except`, read a traceback from the bottom up and know what it is telling you, write your own context manager, and handle a failed network request without the program simply stopping.

You need Chapters 7 and 8 (object-oriented programming) first, because an exception is an object and a context manager is a class.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Question Bank](050-ch9-conceptual-q.md) | The conceptual questions from the end of the chapter, each answered in full | Start here |
| [Forty Script-Based Exercises](060-ch9-scripts-q.md) | Forty programs to write, each with a complete worked answer | Practice |
| [Context Managers: with, \_\_enter\_\_ and \_\_exit\_\_](030-ch9-context-manager.md) | What `with` really does, and how to write a class that works with it | After the chapter's section on `finally` |
| [Digging Into Exceptions: sys and traceback](040-ch9-traceback.md) | Getting at the details of an exception while the program is still running | When a traceback is not enough |
| [Exceptions as Objects: \_\_traceback\_\_](041-ch9-traceback.md) | The traceback is an object too, and what you can do with it | After the page above |
| [Reading Files from the Internet with urllib](010-ch9-urlib.md) | Fetching a file with the standard library, and the errors that come with it | A real use for exceptions |
| [Reading Files from the Internet with requests](020-ch9-requests.md) | The same job with the `requests` library, and how its errors differ | After the `urllib` page |

## Suggested Reading Order

1. **Conceptual Question Bank**, in order. It follows the printed chapter.
2. **Context Managers.** `with` is the tidiest answer to "make sure this gets cleaned up", and you have already been using it for files without knowing how it works.
3. **The two traceback pages**, in order. Together they explain what the wall of text on a crash actually contains.
4. **The two internet pages.** These are where exception handling stops being an exercise: a network request can fail in a dozen ways, and none of them are your program's fault.
5. **The forty exercises** throughout, as practice.

## Three Points Worth Extra Care

**Catch the exception you expect, not all of them.** A bare `except:` hides typing mistakes, keyboard interrupts and bugs you have not found yet. Name the exception: `except FileNotFoundError:`.

**`finally` runs whatever happens** — after a `return`, after an exception, after a `break`. That is what makes it the right place for cleanup, and it is also why a `return` inside `finally` can quietly swallow an exception.

**`with` is a context manager, and you can write your own.** Any class with `__enter__` and `__exit__` works with `with`. Once you have written one, `with open(...)` stops looking like special syntax.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell. Where a script produces output, that output is shown underneath.

Two things will differ on your machine. The two internet pages need a working connection, and the sites they fetch may answer differently or not at all; the point is how your program behaves when that happens. And tracebacks show file paths and line numbers from your own copy of the script, so those lines will not match the page exactly.

The `requests` library does not come with Python. Install it once with `pip install requests`. The `urllib` page needs nothing extra.
