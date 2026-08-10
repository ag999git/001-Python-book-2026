# Python Basics

You can also visit my GitHub repository or the Google Colab notebooks by clicking the badges below

| Book Repository                                                                                                                                                                                  | Interactive Labs                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![Book Repo](https://img.shields.io/badge/GitHub-Full_Book_Repo-3776AB?style=for-the-badge\&logo=github\&logoColor=white\&labelColor=555555)](https://github.com/ag999git/001-Python-book-2026) | [![Colab Folder](https://img.shields.io/badge/Google_Colab-Notebook_Folder-FFD700?style=for-the-badge\&logo=googlecolab\&logoColor=white\&labelColor=228B22)](../colab-nb) |


[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3100/)
[![IDE](https://img.shields.io/badge/IDE-VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Jupyter](https://img.shields.io/badge/Notebooks-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Supported-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)


#### Table of Contents   


* [1 Comparison between Hash and triple quotes](001-python-basics.md#2-comparison-between-hash-and-triple-quotes)
* [2. Good Rules for Writing Identifiers in Python](001-python-basics.md#2-good-rules-for-writing-identifiers-in-python)
* [3. What are PEP and PEP 8 in Python? (Simple Explanation)](001-python-basics.md#3-what-are-pep-and-pep-8-in-python-simple-explanation)
* [4. Table: Identifiers vs Variables](001-python-basics.md#4-table-identifiers-vs-variables)
* [5. Python Keywords — Meaning + Example in form of a Table](001-python-basics.md#5-python-keywords--meaning--example-in-form-of-a-table-are-given-below)
* [6. Debugging](001-python-basics.md#6-debugging-python-scripts-on-an-ide)
* [7. Python Keywords — Meaning, Code Example, Real-Life Analogy](001-python-basics.md#7-python-keywords--meaning-code-example-real-life-analogy)



#### 1 Comparison between Hash and triple quotes

Hash (#) and triple quotes (''' or """)

[Back to Table of Contents](001-python-basics.md#table-of-contents)

**1.1. Hash (#) — Single-Line Comments**

* Starts with # and continues to the end of the line.
* Used mainly for explaining **logic**, **steps**, or **reasoning** inside the code.
* Helpful for programmers who want to **understand, debug, or modify** the code.
* Typically scattered throughout functions and code blocks.
* Can be used for multi-line comments by repeating # on each line.
* Ignored entirely by the Python interpreter.

**1.2. Triple Quotes (''' or """) — Multi-Line Strings Used as Comments**

* Written using triple single quotes ''' or triple double quotes """.
* Technically creates a **multi-line string**, not a true comment — but becomes a "comment" only if unused.
* Mainly used for **docstrings**: documentation for modules, classes, and functions.
* Appears immediately after a def or class statement.
* Describes **usage**, **purpose**, **arguments**, and **returns** — the _user interface_.
* Tools like Sphinx, pydoc, and IDEs can automatically extract them.
* Can also be placed on one line as a single-line docstring.

Comparison Table:-

| Feature / Purpose    | # Single-Line Comment                    | ''’ / """ Multi-Line Comment (Docstring)                        |
| -------------------- | ---------------------------------------- | --------------------------------------------------------------- |
| Syntax               | # comment                                | """ comment """ or ''' comment '''                              |
| Type                 | True comment                             | Multi-line string used as a comment or docstring                |
| Interpreter behavior | Completely ignored                       | Created as a string; ignored only if not assigned or used       |
| Typical use          | Explain logic or code steps              | Document modules, classes, and functions                        |
| Audience             | Programmers modifying/understanding code | Users who want to know how to use the code                      |
| Location             | Anywhere in code                         | Usually immediately after def, class, or module top             |
| Extraction by tools  | Not extracted                            | Automatically extracted by documentation tools                  |
| Best for             | Inline explanations and quick notes      | Official documentation of API/usage                             |
| Multi-line use       | Yes, by repeating # on each line         | Naturally supports multi-line formatting                        |
| Single-line use      | Yes                                      | Possible by placing opening and closing quotes on the same line |

If you as a beginner are unable to follow/ understand some of the points, don’t worry. They will become clear to you as you progress.

#### 2. Good Rules for Writing Identifiers in Python

Follow the basic legal rules [Back to Table of Contents](001-python-basics.md#table-of-contents)

```
These rules are required by Python itself:-

1.  Use letters (A–Z, a–z), digits (0–9), and underscores (_)  
    Example: total_marks, value2, Student_Name
    
2.  Identifier cannot start with a digit  
    1value is wrong, so is 2value
    
3.  value1 is OK
    
4.  Keywords cannot be identifiers  
    Examples you _cannot_ use:  
    for, while, print, break, class etc.
    
5.  No special symbols  
    Cannot use-> age@school, first-name, price$
    
6.  Python is case-sensitive  
    student ≠ Student ≠ STUDENT
```

#### 3. What are PEP and PEP 8 in Python? (Simple Explanation)

[Back to Table of Contents](001-python-basics.md#table-of-contents)

**3.1 PEP = Python Enhancement Proposal**

A **PEP is a document** that explains:

* **new features** to be added to Python
* **how** Python should work
* **guidelines** and **best practices** for writing Python code
* **changes** or **improvements** to the language

**Think of PEPs like a rulebook + suggestion box**\
They help Python stay organized, consistent, and easy to develop.

**Simple example (analogy):**

Imagine a school where teachers write proposals to improve rules:

* "Let’s add a computer lab."
* "Let’s change the uniform color."

Python developers do the same → they write **PEPs** to propose improvements.

**3.2 What is PEP 8**

You can check out details of PEP 8 [here](https://peps.python.org/pep-0008/)

**PEP 8 = The official Style Guide for Python code**

PEP 8 tells Python programmers:

* how to **format** their code
* how to **name** variables, functions, and classes
* how many spaces to use
* where to put blank lines
* how to write code that is clean, readable, and consistent

**Think of PEP 8 like English grammar rules but for Python.**\
Just like grammar makes English easier to read, PEP 8 makes Python code easier for everyone to understand.

**3.3  PEP  8**

* | PEP 8 Topic                       | What It Means                                                                                        | PEP 8 Example (Correct)                                                                      | Non-PEP 8 Example (Incorrect)                                           |
  | --------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
  | Indentation                       | Use 4 spaces per indentation level                                                                   | if x > 5:    print(x)                                                                        | if x > 5:print(x) (with incorrect spacing or tabs in actual code)       |
  | Tabs vs Spaces                    | Prefer spaces over tabs                                                                              | if x > 5:    print(x)                                                                        | if x > 5:    print(x) (using tab character)                             |
  | Maximum Line Length               | Keep lines under 79 characters                                                                       | # Short comment line                                                                         | # Very long comment line that exceeds 79 characters and is hard to read |
  | Blank Lines                       | Use blank lines to separate sections                                                                 | Two blank lines before class or function                                                     | No blank lines between sections                                         |
  | Imports                           | Keep imports at the top, one per line                                                                | <p>import os<br>import sys</p>                                                               | import os, sys                                                          |
  | Import Order                      | Standard library → Third-party → Local                                                               | <p>import os # Standard library<br>import numpy # Third party<br>import mymodule # Local</p> | Random or mixed ordering                                                |
  | Naming Conventions                | <p>For variable use snake_case,<br>For Class name use PascalCase,<br>For Constant use UPPER_CASE</p> | <p>Variable: total_amount,<br>Class: BankAccount,<br>Constant: MAX_SIZE</p>                  | TotalAmount, bank\_account, maxsize                                     |
  | Whitespace Rules                  | Avoid unnecessary spaces                                                                             | a = b + c                                                                                    | a=b+c or a = b + c                                                      |
  | Comments                          | Write clear comments                                                                                 | # Calculate total price                                                                      | <p>#calc price<br>or obvious comments like<br># increment i</p>         |
  | Docstrings                        | Use triple quotes to document functions                                                              | """Returns sum of two numbers."""                                                            | Using # comments instead of docstrings                                  |
  | Code Layout                       | Keep code clean and structured                                                                       | Organised, readable code                                                                     | Messy, inconsistent layout                                              |
  | Boolean Comparisons               | Use direct checks                                                                                    | if is\_ready:                                                                                | if is\_ready == True:                                                   |
  | Compare with None using is/is not | Follow Pythonic way                                                                                  | if x is None:                                                                                | if x == None:                                                           |
  | Function & Variable Names         | Use lowercase\_with\_underscores                                                                     | get\_value(), student\_age                                                                   | GetValue(), StudentAge, studentAge                                      |
  | Class Names                       | Use PascalCase                                                                                       | CarModel                                                                                     | carmodel, car\_model, carModel                                          |
  | Constant Names                    | Use UPPER\_CASE                                                                                      | MAX\_SPEED = 120                                                                             | maxspeed = 120                                                          |
  | Spacing After Commas              | Put a space after commas                                                                             | sum(1, 2, 3)                                                                                 | sum(1,2,3)                                                              |
  | Single Statement per Line         | Use one statement per line                                                                           | <p>x = 1;<br>y = 2 (preferred to split in two lines)</p>                                     | x = 1; y = 2 (not recommended in practice)                              |

**3.4 Pep 8 Vs Non-pep 8 Examples**

[Back to Table of Contents](001-python-basics.md#table-of-contents)

**The following code in Python gives example of use of PEP 8 versus non-PEP 8 for:-**

* Variables
* Functions
* Loops
* Conditionals
* Comments

```python
# ===============================================================
# PYTHON STYLE GUIDE: PEP 8 VS. NON-PEP 8
# This script demonstrates the "Pythonic" way to write code.
# ===============================================================

# ---------------------------------------------------------------
# 1. VARIABLES: The "Identity" of your data
# Rule: Use snake_case (all lowercase with underscores)
# ---------------------------------------------------------------

# PEP 8 STYLE (CORRECT)
# This is easy to read because words are separated by underscores.
student_age = 20
total_score = 95

# CONSTANTS: Use all UPPERCASE to show this value should not change.
MAX_LIMIT = 100

# NON-PEP 8 STYLE (AVOID)
StudentAge = 20  # Avoid starting variables with Capital Letters
totalScore = 95  # This is "camelCase" - common in Java, but not Python
maxlimit = 100    # Hard to read; always use underscores to separate words

print("Section 1: Variable naming conventions demonstrated.")


# ---------------------------------------------------------------
# 2. FUNCTIONS: Actions your code performs
# Rule: Use snake_case and keep it readable
# ---------------------------------------------------------------

# PEP 8 STYLE (CORRECT)
# Use descriptive names and give the code space to "breathe."
def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    return total / 3

# NON-PEP 8 STYLE (AVOID)
# Never put the logic on the same line as the 'def' statement.
def CalculateAverage(score1,score2,score3): total=score1+score2+score3;return total/3

print(f"Section 2: Average is {calculate_average(80, 90, 100)}")


# ---------------------------------------------------------------
# 3. CLASSES: Blueprints for objects
# Rule: Use PascalCase (Capitalize every word, no underscores)
# ---------------------------------------------------------------

# PEP 8 STYLE (CORRECT)
class StudentRecord:
    """Classes represent 'Things' so we capitalize them."""
    pass

class AttendanceManager:
    pass

# NON-PEP 8 STYLE (AVOID)
class studentRecord: # Should be Capitalized
    pass

class Attendance_Manager: # Avoid underscores in class names
    pass

print("Section 3: Class naming (PascalCase) demonstrated.")


# ---------------------------------------------------------------
# 4. CONDITIONALS: Decision making
# Rule: Use spaces around operators and proper indentation
# ---------------------------------------------------------------

x = 10

# PEP 8 STYLE (CORRECT)
# Space around the '>' and the '==' makes it much cleaner.
if x > 5:
    print("Section 4: x is greater than 5")
elif x == 5:
    print("Section 4: x is exactly 5")

# NON-PEP 8 STYLE (AVOID)
# Don't squash code together; it makes debugging very difficult.
if x>5: print("x>5")


# ---------------------------------------------------------------
# 5. INTERNAL NAMES (Advanced)
# Rule: Start with a single underscore for internal/private use
# ---------------------------------------------------------------

# PEP 8 STYLE (CORRECT)
# This tells other programmers: "Use this only inside this script."
def _internal_utility_function():
    return "This is a hidden helper function."

print(f"Section 5: {_internal_utility_function()}")

# ===============================================================
# END OF SCRIPT: All code is PEP 8 compliant and runs perfectly!
# ===============================================================


```

You can run the above script in Google Colab (From Google Drive) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o0MazyhjW0tcmbxILSQXFVWrI8qp-gJ_?usp=sharing)

You can run the above script in Google Colab (Same notebook from GitHub) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ag999git/001-Python-book-2026/blob/main/colab-nb/01Chapter1_pep.ipynb)

#### 4. Table: Identifiers vs Variables

[Back to Table of Contents](001-python-basics.md#table-of-contents)

| Feature                | Identifier                                                 | Variable                                     |
| ---------------------- | ---------------------------------------------------------- | -------------------------------------------- |
| **Definition**         | A name used to identify something in Python                | A memory location that stores a value        |
| **What it represents** | Can represent variables, functions, classes, modules, etc. | Only represents data stored in memory        |
| \*\*Creation \*\*      | Created when you write a name (e.g., myFunc)               | Created only after assignment (e.g., x = 10) |
| **Has value?**         | No                                                         | Yes                                          |
| **Has type?**          | No                                                         | Yes (type of stored value)                   |
| **Has scope?**         | Depends on what it names                                   | Yes — local, global, class-level             |
| **Example**            | sum, my\_list, print, Car                                  | x = 5, name = "Anurag"                       |
| **Error if missing?**  | Undefined identifier → NameError                           | Same, because variable name is an identifier |
| **Used for**           | Naming program components                                  | Storing and manipulating data                |

#### 5. Python Keywords — Meaning + Example in form of a Table are given below

| Keyword    | Meaning / Simple Explanation        | Example Sentence (Code)  | Real-Life Example / Analogy                                 |
| ---------- | ----------------------------------- | ------------------------ | ----------------------------------------------------------- |
| `and`      | Both conditions must be true        | if x > 0 and y > 0:      | “I will go for a walk if it’s sunny and I have free time.”  |
| `or`       | At least one condition must be true | if age < 18 or age > 60: | “I will drink tea or coffee — either one is fine.”          |
| `not`      | Reverses a condition                | if not is\_raining:      | “I will go out not if it’s raining.”                        |
| `if`       | Decision-making                     | if score >= 50:          | “If it’s your birthday, you get a gift.”                    |
| `elif`     | Additional condition                | elif score >= 40:        | “If not birthday, elif it’s festival, you get sweets.”      |
| `else`     | Runs when all conditions fail       | else:                    | “Otherwise, nothing special happens.”                       |
| `for`      | Loop over a sequence                | for n in \[1,2,3]:       | “Give chocolates to each student in class.”                 |
| `while`    | Loop while condition is true        | while count < 5:         | “I study while it’s quiet.”                                 |
| `break`    | Stop the loop                       | if n == 5: break         | “Stop the game if someone gets hurt.”                       |
| `continue` | Skip current iteration              | if n % 2 == 0: continue  | “Skip this person and move to the next.”                    |
| `pass`     | Do nothing                          | def func(): pass         | Calling roll: “Absent? … pass.”                             |
| `def`      | Define a function                   | def add(a, b):           | Writing a recipe: “def make\_tea():”                        |
| `return`   | Send value back                     | return a + b             | At end of recipe: “Serve tea.”                              |
| `lambda`   | Small anonymous function            | square = lambda x: x\*x  | Quick rule: “Multiply by 2” without naming it.              |
| `class`    | Define a class                      | class Car:               | Blueprint for a car model.                                  |
| `import`   | Bring a module                      | import math              | “Bring a tool from the toolbox.”                            |
| `from`     | Import part of a module             | from math import sqrt    | “Bring only the screwdriver from the toolbox.”              |
| `as`       | Give short name to module           | import math as m         | “Call the screwdriver ‘SD’ for short.”                      |
| `try`      | Code that may cause error           | try:                     | “Try opening the door; it might be locked.”                 |
| `except`   | Handle the error                    | except ValueError:       | “If locked, use the key.”                                   |
| `finally`  | Always runs                         | finally:                 | “Before leaving, lock the gate — always.”                   |
| `raise`    | Throw an error                      | raise TypeError("Wrong") | “Raise a complaint if rules are broken.”                    |
| `assert`   | Debug check                         | assert x > 0             | “Check seatbelt is on before driving.”                      |
| `in`       | Check membership                    | if "a" in "apple":       | “Is your name in the list?”                                 |
| `is`       | Check if same object                | if x is None:            | “Two cups look same — are they the same cup?”               |
| `global`   | Use global variable                 | global count             | Taking money from main family wallet.                       |
| `nonlocal` | Use outer function variable         | nonlocal total           | Helper using owner’s cash drawer.                           |
| `with`     | Automatic setup + cleanup           | with open("a.txt") as f: | “With washing machine, wash + clean happens automatically.” |
| `yield`    | Return values one at a time         | yield item               | Tree gives mangoes one by one.                              |
| `del`      | Delete variable/item                | del numbers\[0]          | Throw away old notebook.                                    |
| `exec`     | Execute Python code dynamically     | exec("print('Hello')")   | “Follow these written instructions exactly.”                |
| `print`    | Show output                         | print("Hello")           | Saying something out loud.                                  |

[Back toTable of Contents](001-python-basics.md#table-of-contents)

#### 6. Debugging Python scripts on an IDE

The following flowchart shows how to debug a Python script

![Flowchart for debugging a Python script in an IDE](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/Debugging-chart.png)

**Step-by-step explanation of the debug flowchart**

Below is a short, clear walk-through of each step in the above flowchart. It gives a typical cycle used when debugging in VS Code (or any debugger).

1. Start Debugging\
   Begin the debugging session — open the code you want to inspect.
2. Open Code\
   Make sure the file(s) you want to debug are visible in the editor and the correct project/folder is opened.
3. Set Breakpoints\
   Click the left margin next to one or more lines to place breakpoints (red dots). These tell the debugger where to pause execution.
4. Run Debugger? (Decision)\
   Choose to start the debugger. If not yet started, press F5 or click Run & Debug to launch it.
5. Debugger Starts\
   The program begins running under the debugger’s control (a debug session is active).
6. Breakpoint Hit? (Decision)\
   The debugger checks whether execution reaches a breakpoint:

* Yes → Inspect Variables (execution is paused)
* No → Continue Running (program runs until next breakpoint or end)

8. Inspect Variables\
   While paused, examine variable values by hovering, looking at the _VARIABLES_ panel, or using the _WATCH_ panel. Also check the _CALL STACK_ to know where you are.
9. Continue Running\
   If no breakpoint was hit, let the program continue running (it may hit another breakpoint later).
10. Bug Found? (Decision)\
    After inspection, decide whether the cause of the problem is clear:

* Yes → Fix Code
* No → Add Breakpoints or Logs

12. Fix Code\
    Edit the source to correct the bug (logic error, wrong value, off-by-one, etc.).
13. Test Fix\
    Re-run the debugger (usually by starting again with F5 or using Restart) to verify the change.
14. Working? (Decision)\
    Check whether the program now behaves correctly:

* Yes → End (debugging finished)
* No → Add Breakpoints or Logs (go back into the cycle)

16. Add Breakpoints or Logs\
    If the bug is not yet identified, add more breakpoints or temporary print() / logging statements, then return to Run Debugger? to repeat the cycle.

[Back toTable of Contents](001-python-basics.md#table-of-contents)





#### 7. Python Keywords — Meaning, Code Example, Real-Life Analogy

The following table has 4 columns.

* The first column gives the Python keyword.
* The second column gives Meaning/ Simple explanation for that keyword.
* The third column gives an Example sentence (Code) for that keyword.
* The fourth column gives a Real-life Example/ Analogy for that keyword.

| Keyword  | Meaning / Simple Explanation              | Example Sentence (Code)                    | Real-Life Example / Analogy                                              |
| -------- | ----------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| and      | True only if both conditions are true     | if a > 0 and b > 0: print("Both positive") | Like saying: _I will go only if it’s Saturday **and** it’s not raining._ |
| as       | Give a temporary name to something        | import math as m                           | Like calling your friend "Raj" as "RJ" for convenience.                  |
| assert   | Check if something is true; stop if false | assert age > 0                             | Like a teacher checking “Are you sure?” before proceeding.               |
| break    | Exit a loop immediately                   | for x in arr: break                        | Like stopping a game in the middle.                                      |
| class    | Create a blueprint for objects            | class Car: pass                            | Like a form used to create many ID cards of the same design.             |
| continue | Skip the current loop step                | if x < 0: continue                         | Like skipping one student’s turn and moving to the next.                 |
| def      | Define a function                         | def greet(): pass                          | Like defining a recipe you can use anytime.                              |
| del      | Delete a variable or item                 | del x                                      | Like throwing something away from your cupboard.                         |
| elif     | Extra conditions after “if” fails         | if a>0:… elif a==0:…                       | Like: “If not bus, **else if** auto is available…”                       |
| else     | Runs if all conditions fail               | if rain:… else:…                           | Like: “If none of the above works, do this.”                             |
| except   | Handle errors                             | try:… except:…                             | Like catching a falling glass before it breaks.                          |
| False    | Boolean false value                       | flag = False                               | Like a switch turned OFF.                                                |
| finally  | Code that always runs                     | finally: print("Done")                     | Like always locking your door when leaving home.                         |
| for      | Loop through items                        | for x in nums:…                            | Like checking names one by one in a list.                                |
| from     | Import a specific part of a module        | from math import pi                        | Like taking only one book from a library shelf.                          |
| global   | Declare a variable as global              | global count                               | Like sharing one notebook across all family members.                     |
| if       | Used for conditions                       | if score>50:…                              | Like deciding “If it rains, take umbrella.”                              |
| import   | Bring in external modules                 | import os                                  | Like bringing a toolbox from another room.                               |
| in       | Check membership                          | if 'a' in word:…                           | Like checking if your name is in a list.                                 |
| is       | Check object identity                     | if a is b:…                                | Like checking if two cups are actually the _same_ cup.                   |
| lambda   | Create small anonymous functions          | f = lambda x: x\*2                         | Like writing a one-line rule on a sticky note.                           |
| None     | Represents “nothing"                      | x = None                                   | Like an empty seat with no one sitting.                                  |
| nonlocal | Use a variable from outer function        | nonlocal x                                 | Like borrowing your sibling’s stationery.                                |
| not      | Negation; opposite value                  | if not ready:…                             | Like saying “Not hungry.”                                                |
| or       | True if at least one condition is true    | if rain or snow:…                          | Like “I’ll play if it’s Saturday **or** Sunday.”                         |
| pass     | Empty placeholder                         | if x>0: pass                               | Like noting “To be decided later.”                                       |
| raise    | Throw an error                            | raise ValueError                           | Like raising your hand to report a problem.                              |
| return   | Send back a value from function           | return result                              | Like giving back a filled form.                                          |
| True     | Boolean true value                        | flag = True                                | Like a switch turned ON.                                                 |
| try      | Test risky code                           | try: open(file)                            | Like cautiously testing if water is hot.                                 |
| while    | Loop until condition becomes false        | while x<5:…                                | Like “Keep running while timer is not finished.”                         |
| with     | Simplify resource handling                | with open(...) as f:…                      | Like using a rented car and returning it automatically.                  |
| yield    | Produce value and pause function          | yield x                                    | Like giving items from a box one at a time.                              |







