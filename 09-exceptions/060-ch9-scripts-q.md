


# Chapter 9: Forty Script-Based Exception Exercises

This section complements the conceptual Q&A elsewhere in this chapter with something more hands-on: forty short, self-contained scripts, each built around a single exception-handling idea. Where the conceptual questions asked "why does Python behave this way?", these are "here's a small script — read it, run it, and see that behavior for yourself." They move from the fundamentals (catching a `TypeError`, using `try`/`except`/`else`/`finally`) through the standard built-in exception types, into custom exceptions, and finish with a set of more advanced topics — exception chaining, exception groups, and context managers — marked *(Advanced)* since they build on ideas from later in the chapter.

Each exercise keeps its **original prompt exactly as printed in the book**. The scripts and explanations underneath have been reworked: extra explanation has been added before and after each one, every script now has step-by-step comments, and one real bug from the original file has been fixed — see Exercise 1 below.

A tip on working through these: try writing your own solution to each prompt *before* looking at the answer given here. The value of these exercises is in the attempt, not just in reading the final code.

---

### 1. Write a script that attempts to add a string and an integer. Wrap this in a `try`-`except` block to catch the specific exception and print a helpful message.

> **Note:** the original version of this script had a copy-paste error — a stray fragment of markdown formatting had been accidentally pasted directly into the Python string, which would have caused this script to fail with a `SyntaxError` before it could even demonstrate the `TypeError` it was meant to show. The corrected version below fixes that.

```python
try:
    # Step 1: attempt an operation that mixes incompatible types --
    # Python cannot automatically combine a string and an integer with +
    result = "Total: " + 3

except TypeError as e:
    # Step 2: TypeError is raised because + means different things for
    # different types (concatenation for strings, addition for numbers) --
    # Python won't guess which one you meant here.
    print(f"Error caught: {e}. You cannot add a string to an integer directly.")
```

> **Why this happens:** `+` is *overloaded* in Python — it means "join text together" for strings, but "add numbers" for integers and floats. Since Python doesn't automatically convert one type into the other, mixing them with `+` is treated as an error rather than a guess. If you actually want to combine them, you'd explicitly convert first: `"Total: " + str(3)`.

---

### 2. Create a script that asks a user for their age. Use the `raise` statement to trigger a `ValueError` if the age is less than 0, and handle it.

```python
try:
    # Step 1: get input from the user (always returns a string)
    user_age = int(input("Enter your age: "))   # may also raise ValueError if not a number at all

    # Step 2: check a business rule Python itself has no concept of --
    # a negative age isn't a Python error, but it IS a logical one.
    if user_age < 0:
        raise ValueError("Age cannot be a negative number.")

    print(f"Age recorded: {user_age}")

except ValueError as e:
    # Step 3: this catches BOTH the manual raise above AND a failed
    # int() conversion (e.g. if the user typed "abc" instead of a number)
    print(f"Validation Error: {e}")
```

> This is a direct example of a manual sanity check, discussed in more depth in the conceptual Q&A (Question 27) — Python is happy to store `-5` in a variable, but your program's own logic isn't.

---

### 3. Demonstrate the difference between a Syntax Error and an Exception by writing a script that attempts to divide by zero. Explain via comments why this is an Exception and not a Syntax Error.

```python
# Step 1: a Syntax Error would prevent this code from running AT ALL --
# for example, a missing colon after 'try', or a mismatched bracket.
# This script has none of those problems, so it parses and starts fine.

try:
    # Step 2: the error below only happens once this line actually
    # RUNS -- Python has no way of knowing in advance that num2 will
    # be zero just by reading the code structurally.
    calculation = 10 / 0

except ZeroDivisionError:
    # Step 3: this is an EXCEPTION, not a syntax error, because the
    # code was perfectly valid Python -- the problem only appeared
    # once a specific operation was carried out with a specific value.
    print("Logic Error: You cannot divide a number by zero.")
```

---

### 4. Write a script using `try`, `except`, and `else`. The script should divide two numbers; the `else` block should print the result only if no error occurred.

```python
try:
    # Step 1: the operation that might fail
    num1 = 10
    num2 = 2
    ans = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    # Step 2: runs ONLY if the try block completed with no exception --
    # this keeps "what to do on success" cleanly separate from
    # "what might go wrong"
    print(f"Division successful! The result is: {ans}")
```

---

### 5. Create a script that tries to access a non-existent file. Handle both `FileNotFoundError` and `PermissionError` separately.

```python
try:
    # Step 1: attempt to open a file that likely doesn't exist
    with open("ghost_file.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    # Step 2: the file simply isn't there
    print("The system could not find the specified file.")

except PermissionError:
    # Step 3: the file exists, but this program isn't allowed to read it --
    # a genuinely DIFFERENT problem, worth reporting separately
    print("You do not have the required permissions to read this file.")
```

> Both of these are subclasses of the broader `OSError` — see the conceptual Q&A (Question 17) for when it's better to catch that shared parent instead of each one individually.

---

### 6. Write a script that uses a `finally` block to ensure a "Cleanup Complete" message prints regardless of whether a `ValueError` occurs during a string-to-int conversion.

```python
try:
    # Step 1: risky conversion -- "abc" cannot become an integer
    val = int("abc")

except ValueError:
    print("Conversion failed: Invalid literal for integer.")

finally:
    # Step 2: this line runs whether the conversion succeeded, failed,
    # or even if some OTHER, uncaught exception had occurred instead
    print("Cleanup Complete: Releasing resources and closing sessions.")
```

---

### 7. Demonstrate the "Generic Exception" safety net. Write a script with a specific `except` for `IndexError` and a generic `except Exception as e` for any other unforeseen errors.

```python
try:
    my_list = [1, 2, 3]
    # Step 1: index 10 is well beyond this list's valid range (0, 1, 2)
    print(my_list[10])

except IndexError:
    # Step 2: the specific, expected failure gets its own clear message
    print("Specific Error: Index is out of range.")

except Exception as e:
    # Step 3: a fallback for anything else -- placed LAST, so it never
    # intercepts the more specific IndexError block above it
    print(f"An unexpected error occurred: {e}")
```

---

### 8. Explain the risk of a "bare" `except:` clause. Write a script that uses one, and add a comment explaining why catching `KeyboardInterrupt` accidentally is bad.

```python
import time

try:
    while True:
        print("Running... (Try pressing Ctrl+C)")
        time.sleep(1)

except:
    # DANGER: a bare 'except:' catches EVERYTHING, including
    # KeyboardInterrupt (raised when the user presses Ctrl+C).
    # That means the user may not even be able to stop this program
    # the normal way -- a serious usability and safety problem.
    print("Caught something, but I don't know what. This is bad practice!")
```

> A safer alternative, if you genuinely want to react to Ctrl+C specifically, is shown in Exercise 28 below — catch `KeyboardInterrupt` *by name*, never with a bare `except:`.

---

### 9. Write a script that demonstrates the `as` keyword. Catch a `ZeroDivisionError` and use the alias to print the arguments (`args`) stored inside the exception object.

```python
try:
    result = 5 / 0

except ZeroDivisionError as e:
    # Step 1: 'e' is a full exception OBJECT, not just a message string
    print(f"Exception Type: {type(e)}")

    # Step 2: .args is a tuple holding the raw values the exception
    # was created with -- usually just the message, in a 1-item tuple
    print(f"Arguments provided to exception: {e.args}")
```

---

### 10. Use the `with` statement (Context Manager) to open a file. Write a comment explaining why this is safer than manual `f.close()` in terms of exceptions.

```python
try:
    # Step 1: 'with' automatically calls the file's cleanup code
    # (closing it) once this block ends -- successfully OR via an
    # exception. A manual f = open(...); ... ; f.close() approach
    # would SKIP the close() call entirely if an exception occurred
    # before reaching that line.
    with open("sample.txt", "w") as f:
        f.write("Hello World")
        # if a crash happened right here, 'with' would still
        # close the file safely on the way out

except IOError as e:
    print(f"File error: {e}")
```

> This section of the book covers custom context managers — building your own `__enter__`/`__exit__` classes — in full detail elsewhere in this chapter, if you'd like to see exactly how `with` accomplishes this guarantee.

---

### 11. Create a dictionary and attempt to access a missing key. Catch the `KeyError` and use the `else` block to confirm the data was found.

```python
data = {"name": "Alice", "role": "Admin"}

try:
    # Step 1: "id" was never added to this dictionary
    user_id = data["id"]

except KeyError as e:
    # Step 2: e here is just the missing key itself, e.g. 'id'
    print(f"Key Error: The key {e} was not found in the dictionary.")

else:
    # Step 3: only reached if the lookup succeeded
    print(f"Data retrieved: {user_id}")
```

---

### 12. Demonstrate handling multiple exceptions in a single tuple. Catch `ValueError` and `TypeError` in one block for a script that processes user input.

```python
def process_input(data):
    try:
        # Step 1: int(None) raises TypeError; int("xyz") raises ValueError --
        # two DIFFERENT exception types from the same line of code
        value = int(data)
        print(f"Processed: {value}")

    except (ValueError, TypeError):
        # Step 2: grouping related errors in a tuple lets one block
        # respond to either, when the appropriate reaction is the same
        print("Input Error: Please provide a valid numeric string.")


process_input(None)     # TypeError
process_input("xyz")    # ValueError
```

---

### 13. Show the correct order of handling a Parent and Child exception. Define a custom `ParentError` and a `ChildError`, then catch them in the correct sequence.

```python
class ParentError(Exception):
    """A general application error."""
    pass


class ChildError(ParentError):
    """A more specific problem -- ChildError IS-A ParentError."""
    pass


try:
    raise ChildError("Specific problem occurred")

except ChildError:
    # Step 1: the MORE SPECIFIC exception type must be checked first
    print("Caught the specific ChildError.")

except ParentError:
    # Step 2: this only catches ParentErrors that AREN'T also ChildErrors
    print("Caught a general ParentError.")
```

---

### 14. Show the "Incorrect" order of Parent/Child handling and explain via comments why the `ChildError` block becomes unreachable.

```python
class ParentError(Exception):
    pass


class ChildError(ParentError):
    pass


try:
    raise ChildError("Specific problem")

except ParentError:
    # Step 1: Python checks except blocks top to bottom, and since
    # ChildError IS-A ParentError (through inheritance), THIS block
    # matches first and catches it -- even though it's the less
    # specific handler.
    print("Caught by Parent block.")

except ChildError:
    # Step 2: UNREACHABLE CODE. By the time Python would check this
    # block, the exception has already been caught above -- this
    # line will never run, no matter what.
    print("Caught by Child block.")
```

![Flowchart](/resources/ch-9-exceptions-august-2026-scripting-question-bank01.png)




---

### 15. Write a script that defines a custom exception `InsufficientFundsError` that takes `balance` and `amount` in its `__init__` method.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

    def __init__(self, balance, amount):
        # Step 1: store the specific data relevant to THIS error
        self.balance = balance
        self.amount = amount

        # Step 2: still pass a readable message up to the base
        # Exception class, so str(e) and print(e) work sensibly
        super().__init__(f"Attempted to withdraw {amount} with balance {balance}")


try:
    raise InsufficientFundsError(100, 500)

except InsufficientFundsError as e:
    # Step 3: the custom attributes are available directly on 'e'
    print(f"Custom Data: Balance={e.balance}, Requested={e.amount}")
```

---

### 16. Implement the `__str__` method in a custom exception class to provide a formatted error message when the object is printed.

```python
class NetworkError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        # Step 1: this runs automatically whenever the exception
        # object is printed, or converted with str()
        return f"[Network Error Code: {self.code}] Connection timed out."


try:
    raise NetworkError(404)

except NetworkError as e:
    # Step 2: print(e) implicitly calls e.__str__() -- this is
    # what actually produces the formatted message above
    print(e)
```

---

### 17. Write a script that demonstrates `ImportError` by trying to import a non-existent module. Handle `ModuleNotFoundError` specifically.

```python
try:
    import mythical_module   # this module does not actually exist

except ModuleNotFoundError:
    # Step 1: ModuleNotFoundError is a SUBCLASS of ImportError --
    # specifically for "the module simply isn't there at all"
    print("Error: The requested module 'mythical_module' does not exist.")

except ImportError:
    # Step 2: catches the broader category -- e.g. the module WAS
    # found, but something inside it failed to load correctly
    print("Error: A general import error occurred.")
```

---

### 18. Illustrate `AttributeError` by attempting to call a method that does not exist on a string object.

```python
text = "Hello"

try:
    # Step 1: strings don't have a .push() method -- that's a list-like
    # operation, and Python objects only support the methods their
    # class actually defines
    text.push("World")

except AttributeError as e:
    print(f"Object Error: {e}")
```

---

### 19. Demonstrate `NameError` by trying to print a variable that hasn't been defined yet.

```python
try:
    # Step 1: 'secret_key' was never assigned a value anywhere
    # before this line -- Python has no idea what it refers to
    print(secret_key)

except NameError as e:
    print(f"Variable Error: {e}. Ensure variables are defined before use.")
```

---

### 20. Write a script that catches `IndexError` when iterating through a list and trying to access an element beyond its length.

```python
my_list = [10, 20]

try:
    # Step 1: valid indices here are only 0 and 1 -- index 2 is
    # one position past the end of this 2-item list
    item = my_list[2]

except IndexError:
    print("List Error: You are trying to access a position that doesn't exist.")
```

---

### 21. Use `raise` to re-raise an exception after logging it locally.

```python
try:
    x = 1 / 0

except ZeroDivisionError as e:
    # Step 1: do something local first -- here, just a print,
    # but this could just as easily be writing to a log file
    print("Logging locally: Someone tried to divide by zero.")

    # Step 2: a bare 'raise' re-raises the SAME exception that was
    # just caught, so it continues propagating to whatever code
    # called this one -- see the conceptual Q&A (Question 13) for
    # why this "layered" handling is often useful
    raise
```

---

### 22. Create a script that uses `EOFError` to handle a situation where `input()` is interrupted (e.g., by pressing Ctrl+D).

```python
try:
    # Step 1: input() normally waits for the user to type something
    # and press Enter -- but if the input stream ends unexpectedly
    # (e.g. Ctrl+D on Linux/Mac, or piped input running out), Python
    # raises EOFError instead of returning a string
    data = input("Enter data (or press Ctrl+D to exit): ")
    print(f"User entered: {data}")

except EOFError:
    print("\nEnd of file reached. Exiting program gracefully.")
```

---

### 23. Write a function that calculates a square root. Raise a `ValueError` if the input is negative, and catch it in the calling code.

```python
import math

def get_sqrt(n):
    # Step 1: a manual sanity check -- math.sqrt() itself would
    # already raise ValueError for negative input, but checking it
    # explicitly here lets us provide a clearer, custom message
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(n)


try:
    print(get_sqrt(-9))

except ValueError as e:
    print(f"Math Error: {e}")
```

---

### 24. Demonstrate the hierarchy of `ArithmeticError`. Catch `ZeroDivisionError` specifically and then catch `ArithmeticError` as a fallback.

```python
try:
    val = 10 / 0   # triggers ZeroDivisionError specifically

except ZeroDivisionError:
    # Step 1: the most common, specific arithmetic failure
    print("Specific: Zero Division caught.")

except ArithmeticError:
    # Step 2: the shared parent class -- would also catch
    # OverflowError, FloatingPointError, and similar math errors
    print("General: An arithmetic error occurred.")
```

---

### 25. Write a script that checks if a directory exists using `OSError`.

```python
import os

try:
    # Step 1: this fails if the path doesn't exist, OR if it exists
    # but this program lacks permission to read it -- OSError covers
    # BOTH situations at once
    os.listdir("/root/hidden")

except OSError as e:
    print(f"System Error: {e}")
```

---

### 26. Show how `TypeError` occurs when trying to iterate over an integer.

```python
number = 12345

try:
    # Step 1: a for loop needs something ITERABLE -- lists, strings,
    # and ranges all qualify, but a plain integer does not
    for digit in number:
        print(digit)

except TypeError:
    print("Type Error: Numbers are not iterable. Convert to string first.")
    # Tip: str(number) WOULD be iterable, one character at a time
```

---

### 27. Write a script that demonstrates that `finally` runs even if a `return` statement is executed in the `try` block.

```python
def check_finally():
    try:
        print("Inside try block")
        return "Returning from try"   # Python "remembers" this value...

    finally:
        # Step 1: ...but runs THIS block first, before actually
        # handing the return value back to the caller
        print("Finally block executing after return statement!")


result = check_finally()
print(result)
```

![Flowchart](/resources/ch-9-exceptions-august-2026-scripting-question9.png)


---

### 28. Use a generic except to catch a `KeyboardInterrupt` and print "User aborted", but add a comment explaining why this is usually avoided.

```python
import time

try:
    time.sleep(10)

except KeyboardInterrupt:
    # Catching KeyboardInterrupt BY NAME, deliberately, is fine --
    # it's a conscious choice to react to Ctrl+C specifically.
    # What's usually avoided is catching it ACCIDENTALLY through a
    # bare 'except:' or an overly broad 'except Exception:' block
    # (see Exercise 8), which silently swallows it along with
    # everything else.
    print("User aborted the process.")
```

---

### 29. Illustrate `IndentationError` logic. Explain via comments why this cannot be caught with `try`-`except`.

```python
# The following code WOULD cause an IndentationError if actually run
# (shown here only as a comment, since it can't be included as
# real, working code in this script):
#
#     try:
#         if True:
#         print("Missing indent")
#     except IndentationError:
#         print("Caught!")
#
# EXPLANATION: IndentationError is a SUBCLASS of SyntaxError.
# It's detected while Python is PARSING the file -- before a single
# line of it actually runs. Since the file never finishes loading,
# the try/except above never even gets a chance to execute -- there
# is no way to catch a syntax error in the very same file it
# appears in.
```

---

### 30. Create a script that retrieves the name of the exception class dynamically using `type(e).__name__`.

```python
try:
    int("abc")

except Exception as e:
    # Step 1: type(e) gives the exception's CLASS -- e.g. <class 'ValueError'>
    # Step 2: .__name__ gives just the plain text name -- "ValueError"
    # This is especially handy for generic logging code that doesn't
    # know in advance which specific exception type it will catch.
    error_type = type(e).__name__
    print(f"Caught an error of type: {error_type}")
```

---

### 31. *(Advanced)* Use Python 3.11's `ExceptionGroup` to raise multiple exceptions at once.

```python
# ExceptionGroups let a program raise SEVERAL unrelated exceptions
# together, as one bundle -- useful when multiple independent
# checks or tasks can each fail on their own. See the conceptual
# Q&A (Question 33) for more on when this is used in practice.

try:
    raise ExceptionGroup("Validation Failures", [
        ValueError("Invalid age"),
        TypeError("Invalid name type"),
        KeyError("Missing ID"),
    ])

except ExceptionGroup as eg:
    print(f"Caught a group: {eg.message}")

    # Step 1: .exceptions holds every individual error in the bundle
    for e in eg.exceptions:
        print(f" - Sub-error: {e}")
```

---

### 32. *(Advanced)* Demonstrate the `except*` syntax to handle specific errors within an `ExceptionGroup`.

```python
try:
    raise ExceptionGroup("Multi-Error", [ValueError("Bad Value"), TypeError("Bad Type")])

except* ValueError as eg:
    # Step 1: except* filters OUT just the matching exception type(s)
    # from the group, rather than catching the whole group at once
    print("Handled the ValueErrors from the group.")

except* TypeError as eg:
    print("Handled the TypeErrors from the group.")
```

---

### 33. *(Advanced)* Use the `add_note()` method to attach extra debugging information to an exception.

```python
try:
    raise ValueError("Initial Error")

except ValueError as e:
    # Step 1: add_note() attaches EXTRA context, without changing
    # the exception's original message at all
    e.add_note("Context: This occurred during the database sync phase.")

    # Step 2: re-raising now shows the note ALONGSIDE the original
    # traceback, once this propagates and is eventually printed
    raise
```

---

### 34. *(Advanced)* Demonstrate "Exception Chaining" using `raise ... from`.

```python
try:
    1 / 0   # the original, low-level error

except ZeroDivisionError as e:
    # Step 1: wrap the low-level error in a clearer, higher-level one
    # Step 2: 'from e' preserves a link back to the ORIGINAL exception,
    # stored in the new exception's __cause__ attribute -- so nothing
    # about the original failure is lost, even though a different,
    # more meaningful exception is what actually gets raised
    raise RuntimeError("Application failed to process data") from e
```

---

### 35. *(Advanced)* Use `raise ... from None` to suppress the context of a previous exception.

```python
try:
    int("hello")

except ValueError:
    # Using 'from None' deliberately HIDES the fact that a ValueError
    # happened first -- only the new RuntimeError will be shown.
    # Use this sparingly: it's meant for cases where the original,
    # low-level error genuinely isn't useful information for
    # whoever eventually sees this traceback.
    raise RuntimeError("A clean error occurred without showing context") from None
```

---

### 36. *(Advanced)* Use the `traceback` module to print the full stack trace as a string without crashing the program.

```python
import traceback

try:
    result = 10 / 0

except ZeroDivisionError:
    # Step 1: capture the FULL traceback as a plain string, instead
    # of letting Python print it and stop the program
    error_stack = traceback.format_exc()

    print("Program did not crash, but here is the log:")
    print(error_stack)
```

> This section of the book covers `sys.exc_info()`, `e.__traceback__`, and the `traceback` module in much greater depth in the two chapters specifically dedicated to them.

---

### 37. *(Advanced)* Create a custom Context Manager using a class with `__enter__` and `__exit__`.

```python
class MyResource:
    def __enter__(self):
        # Step 1: runs at the START of the 'with' block
        print("Resource Acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Step 2: runs at the END of the 'with' block, whether it
        # finished normally or an exception occurred
        print("Resource Released")

        if exc_type:
            print(f"An error occurred: {exc_val}")

        # Step 3: returning True here SUPPRESSES the exception --
        # execution continues normally after the 'with' block
        return True


with MyResource():
    print("Doing work...")
    raise ValueError("Work failed")

print("Program continues -- the exception above was suppressed.")
```

> The full mechanics of `__enter__`/`__exit__`, including a worked example with a real file, are covered in this chapter's dedicated context-managers section.

---

### 38. *(Advanced)* Use `contextlib.suppress` to ignore a specific exception silently.

```python
from contextlib import suppress
import os

# Step 1: this is a compact alternative to writing a full
# try/except/pass block, specifically for cases where you
# genuinely want to ignore ONE particular, expected exception type
with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")
    print("This line runs, but nothing happens if the file is missing.")
```

> **A word of caution:** this is one of the few places where silently ignoring an exception is considered acceptable practice — but only because it names one *specific*, genuinely expected exception type. Compare this to the dangers of silently swallowing *everything*, covered in the conceptual Q&A (Question 35).

---

### 39. *(Advanced)* Demonstrate how to handle nested `try`-`except` blocks where an inner exception is caught and a different one is raised.

```python
try:
    try:
        # Step 1: the INNER risky operation
        open("none.txt", "r")

    except FileNotFoundError:
        # Step 2: caught locally, and DELIBERATELY converted into a
        # different, more meaningful exception for the outer code
        print("Inner: File missing. Raising ValueError instead.")
        raise ValueError("Configuration missing")

except ValueError as e:
    # Step 3: the OUTER block only ever sees the converted ValueError --
    # it has no idea a FileNotFoundError was involved at all
    print(f"Outer: Caught converted exception: {e}")
```

![Flowchart](/resources/ch-9-exceptions-august-2026-scripting-question39.png)


---

### 40. *(Advanced)* Write a script that checks for "MRO" (Method Resolution Order) issues in custom exceptions when multiple inheritance is used.

```python
class Base(Exception):
    pass


class Mixin:
    pass


class CustomError(Base, Mixin):
    # Step 1: this class inherits from TWO parents at once --
    # Base (an Exception) and Mixin (a plain, ordinary class)
    pass


try:
    raise CustomError("Testing MRO")

except CustomError as e:
    # Step 2: .mro() shows the exact ORDER Python uses to look up
    # methods and attributes across this chain of inheritance
    print(f"Exception Class Hierarchy: {CustomError.mro()}")
    print("Custom Error caught successfully.")
```

> **New term — "MRO" (Method Resolution Order):** when a class inherits from more than one parent (called **multiple inheritance**), Python needs a well-defined order to search through when looking up a method or attribute — this order is the MRO. `ClassName.mro()` lets you inspect that order directly. This is a fairly advanced OOP topic; see the [official Python docs on MRO](https://docs.python.org/3/glossary.html#term-method-resolution-order) if you'd like to go deeper into how it's calculated.




