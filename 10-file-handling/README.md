# Chapter 10: File Handling

The online companion to Chapter 10 of the book. The printed chapter covers opening a file, the modes, reading and writing, and closing properly. These pages carry forty conceptual questions and thirty script exercises, a full reference for `open()` and the file object, and a series of research projects on the parts that repay a closer look: `seek()`, pickling, JSON, the `os` module and the standard streams.

By the end of these pages you should know which mode to open a file in without guessing, understand why a text file and a binary file behave differently under `seek()`, be able to choose between JSON and pickle for saving data, and know how to walk a folder tree.

You need Chapter 9 (exceptions) first, because almost every file operation can fail.

## The Reference Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [File Handling: A Concepts Reference](010-ch10-concepts.md) | Every term in one table, the life of a file from open to close, and worked examples of the important ones | Start here |
| [Text Files versus Binary Files](020-ch10-text-binary.md) | How the two differ, a comparison table, and how to decide which mode you need | Early |
| [A Comprehensive Study of open()](030-ch10-file-open.md) | Every parameter of `open()`, what the file object gives you, and which exception to expect when | Reference |
| [File Capability Methods](050-ch10-file-capability.md) | `readable()`, `writable()`, `seekable()` and what they tell you about an open file | After `open()` |

## The Question Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Conceptual Questions](110-ch10-conceptual.md) | Forty questions in two parts, the second on best practice | Revision |
| [Script Questions](120-ch10-scripts.md) | Twenty programs from the chapter, plus ten on advanced topics | Practice |

## The Research Projects

Each of these is a complete small project: a question, the reasoning, then a script.

| Project | What it investigates |
| --- | --- |
| [seek(offset, whence)](040-ch10-seek.md) | Why seeking works freely in a binary file but is restricted in a text one |
| [The os Module](060-ch10-os-module.md) | Working with paths, folders and the file system itself |
| [Standard Streams](070-ch10-standard-streams.md) | `stdin`, `stdout` and `stderr`, and how data flows through a program |
| [Advanced Pickling](080-ch10-pickling.md) | Saving Python objects to disk and reading them back |
| [JSON versus Pickle](090-ch10-json-pickle.md) | A comparison with a table and worked examples, and how to choose |
| [Inserting Data at Any Position in a File](100-ch10-file-insertion.md) | Why you cannot simply insert into the middle of a file, and the algorithms that get round it |
| [LBYL versus EAFP](130-ch10-lbyl-eafp.md) | "Look before you leap" against "easier to ask forgiveness", and which Python prefers |
| [Walking a Folder Tree with os.walk](140-ch10-oswalk.md) | Visiting every file in every subfolder |

## Suggested Reading Order

1. **The Concepts Reference**, then **Text versus Binary**. These two settle the vocabulary.
2. **The study of open()**, at least the modes table. Opening a file in the wrong mode is the commonest file bug there is, and `'w'` destroys the file's contents the moment it succeeds.
3. **The Conceptual Questions**, Part 1.
4. **The Script Questions**, Part 1, as practice.
5. **The research projects**, in whatever order interests you. `seek()`, then pickling and JSON, is a natural path.
6. **LBYL versus EAFP** once you have written a few file programs and met the errors for yourself.

## Three Points Worth Extra Care

**Mode `'w'` empties the file immediately.** Not when you write, but when you open. If you meant to add to the file, you wanted `'a'`.

**Always close the file, and the reliable way is `with`.** A file left open may not have your data on disk yet, because the write is buffered. `with open(...) as f:` closes it for you even if something goes wrong inside the block.

**Pickle will run code from the file it loads.** It is fine for data your own program saved. Never unpickle a file you did not create yourself. The JSON page explains when JSON is the safer choice.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file or a notebook cell.

These scripts create, change and delete files in whatever folder you run them from. Run them in a scratch folder, not among files you care about. A few of the `os` examples print paths from your own machine, so those lines will not match the page.

