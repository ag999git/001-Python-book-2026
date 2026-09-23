
# Chapter 20: Pytest (Unit Testing)

The online companion to Chapter 20 of the book. The printed chapter takes you from your first `assert` to fixtures, mocking and parameterized tests. These pages carry the longer explanations, the complete worked projects, and full answers to every question at the end of the chapter.

By the end of these pages you should be able to write tests that are independent of one another, prepare and clean up test data with fixtures, replace slow or external things with mocks, check that your code refuses bad input, and run one test against many inputs without repeating yourself.

You need to be comfortable with functions, classes and exceptions before starting.

## The Pages

| Page | What it covers | Best for |
| --- | --- | --- |
| [Common Pytest Command-Line Flags](010-ch20-pytest-flags.md) | `-v`, `-s` and `-k`: what each shows you, why pytest hides `print()` output by default, and how to combine them | Start here |
| [Breaking Free from Rigid Test Classes](020-ch20-unittest-disadvantage-rigid-oop-style.md) | Why the old `setup_method` and `teardown_method` style constrains you, and how fixtures remove the constraint | The idea behind fixtures |
| [Dependency Injection in Pytest Fixtures](040-ch20-dependency-injection.md) | How a test simply names what it needs and pytest supplies it, compared with building the object by hand | Read with the page above |
| [Advanced Fixture Lifecycles: Session Scope](030-ch20-payment-gateway.md) | When creating a fixture once per test is too slow, what the four scopes mean, and the contamination risk that comes with sharing | After fixtures make sense |
| [Sharing Fixtures with conftest.py](065-ch20-conftest-py.md) | Putting a fixture in one place so every test file can use it, without importing anything | When your suite outgrows one file |
| [Testing User Validation with pytest.raises()](060-ch20-user-registration.md) | A registration function that rejects bad input, and the tests that prove it does | Testing for failure |
| [Why pytest.raises Is Better Than try/except](070-ch20-pytest-raises-vs-try-except.md) | Three ways to test an exception, side by side, and why the first two quietly pass when they should fail | Read with the page above |
| [MagicMock: An Introduction](067-ch20-magicmock.md) | Faking objects that support `len()`, iteration, `in` and `with`, which plain `Mock` cannot do | After the book's section on Mock |
| [The "Micro-Precision" Tax Calculator](080-ch20-tax-collector-project.md) | A project in three rounds: repetitive tests, then parameterized tests, then the floating-point trap and `pytest.approx()` | A complete worked project |
| [A Beginner's Guide to pytest.ini and pyproject.toml](090-ch20-config-files.md) | Where pytest keeps its settings, how to register your own markers, and how to stop typing the same flags every time | Tidying up a real project |
| [Conceptual Questions and Answers](095-ch20-conceptual-qa.md) | Twenty questions with full answers, grouped by topic from testing basics through to organising a suite | Revision |
| [Scripting Questions and Answers](097-ch20-scripting-qa.md) | Twenty questions that ask you to write the code, with complete working answers | Practice |

## Suggested Reading Order

1. **Command-Line Flags**, so you can see what your tests are doing.
2. **Rigid Test Classes**, then **Dependency Injection**. These two explain why fixtures exist; read them together.
3. **Session Scope** and **conftest.py** once fixtures feel natural.
4. **User Validation** and **pytest.raises vs try/except** together, in that order.
5. **MagicMock** after the printed chapter's section on `Mock`.
6. **The Tax Calculator project** as a single sitting. It ties parameterized testing to a real bug.
7. **Configuration files** when you start a project of your own.
8. **Conceptual** and **Scripting Questions** for revision and practice.

## Running the Scripts

The scripts on these pages are not loose files. Each one belongs to a small project folder in this directory, because pytest needs a folder structure to discover tests in:

| Folder | Used by |
| --- | --- |
| `pytest-demo/` | Rigid test classes, fixtures |
| `di-demo/` | Dependency injection |
| `payment-demo/` | Session scope |
| `config-demo/`, `banking_project/`, `warning-demo/` | Configuration files |
| `registration-demo/`, `raises-demo/` | User validation and exception testing |
| `magicmock-demo/` | MagicMock |
| `tax-demo/` | The tax calculator project |
| `qa-demo/` | The question pages |

To run any of them, open a terminal in that folder and type `pytest`, adding `-v` to see each test by name or `-s` to see `print()` output. Each page says which folder its scripts belong to and which command to use.




