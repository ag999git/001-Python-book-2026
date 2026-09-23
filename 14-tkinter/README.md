# Chapter 14: GUI Programming with Tkinter

The online companion to Chapter 14 of the book. Tkinter ships with every standard Python installation, so it needs no separate install. It is the natural way to turn a script that only prints to a console into a program with a window, buttons and menus that anyone can use.

The printed chapter covers the widgets and the main loop. These pages go further: the window itself and its lifecycle, the container widgets in full, the one mistake that makes images vanish, delayed callbacks, and error handling in a program that must not simply stop. They also carry the full answers to every question at the end of the chapter.

You need Chapters 7 and 8 (object-oriented programming) first, and Chapter 9 (exceptions) for the error-handling pages.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Advanced Window Configuration and Lifecycle](040-ch14-advance-window-config.md) | Sizing, position, resizing rules, full screen, and closing a window properly | After the printed chapter |
| [Container Widgets: A Reference](045-ch14-container-widgets.md) | Every Tkinter and ttk container in one place: Frame, LabelFrame, PanedWindow, Notebook and the rest | Look-up while building |
| [Why Tkinter Images Disappear](050-ch14-photoimage.md) | `PhotoImage`, variables and garbage collection: the single most confusing bug for beginners | The first time an image will not show |
| [Delayed Tasks, Safe Callbacks and Extra Windows](060-ch14-tkinter-errors2.md) | `after()`, callbacks that outlive their window, and Toplevel windows | When your program uses a timer |
| [Uncaught Exceptions and sys.excepthook](070-ch14-global-error.md) | Catching the errors that would otherwise vanish into the console | Read with the page below |
| [Safe and Unsafe Delayed Callbacks](080-ch14-safe-unsafe-error-after.md) | What goes wrong when an `after()` job fires after its widget is gone, and how to cancel cleanly | After the `after()` page |
| [Professional Error Handling](090-ch14-advanced-error.md) | Logging, global hooks and live validation together in one worked program | The whole picture |
| [Conceptual Questions and Answers](095-ch14-conceptual-qa.md) | Twenty questions with full answers, on widgets, geometry managers, variables and events | Revision |
| [Scripting Questions and Answers](097-ch14-scripting-qa.md) | Worked programs, topic by topic, each complete and ready to run | Practice |

## Suggested Reading Order

1. **Window Configuration**, to get a window behaving the way you want before you put anything in it.
2. **Container Widgets** as a reference rather than a read-through. Come back to it when you need a particular container.
3. **Why Tkinter Images Disappear** early, even if you are not using images yet. The bug it explains wastes more beginner hours than any other in Tkinter.
4. **The three error-handling pages in order**: delayed tasks, then `sys.excepthook`, then safe and unsafe callbacks, then the professional page that puts them together.
5. **Conceptual and Scripting Questions** for revision and practice.

## Three Points Worth Extra Care

**Keep a reference to every `PhotoImage`.** If the only reference is a local variable inside a function, Python collects the image the moment the function returns, and the label shows nothing — with no error at all. Store it on the widget or on `self`.

**Never mix `pack()` and `grid()` in the same container.** Tk raises `TclError` at once. Different containers may use different managers, so a frame can be packed into the root while everything inside that frame uses grid.

**An error inside a callback does not stop the program.** Tkinter catches it, prints a traceback to a console the user is probably not looking at, and carries on. The user clicks a button and nothing happens. Point both `root.report_callback_exception` and `sys.excepthook` at one handler so that every error reaches the user.

## Using the Code

Every script is complete and ready to run. Copy it into a `.py` file and run it from a terminal.

These scripts open a window, so they will not run inside a notebook cell or in Google Colab. Run them on your own computer. Where a page shows what the window looks like, that is a screenshot, not printed output.

