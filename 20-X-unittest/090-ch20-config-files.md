



## Understanding the "Unknown Marker" Warning

Have you ever used a custom marker like `@pytest.mark.slow` and seen a warning in your terminal saying `PytestUnknownMarkWarning`? This warning appears because pytest doesn’t know what "slow" means yet—it hasn't been introduced to it.

The fix is a simple text file named `pytest.ini` (or `pyproject.toml`). This file acts as a "settings menu" for your project. It tells pytest where your markers are, which default flags to use, and how to behave consistently across different computers.

To learn how to silence that warning, register your markers, and keep your team's test runs identical, check out the detailed guide on the GitHub repository. It includes step-by-step setup, a comparison of file formats, and a "No-Warning" cheat sheet.

## A Beginner's Guide to `pytest.ini` and `pyproject.toml`

----------

### 1. What is a Configuration File? (The Everyday Analogy)

Imagine you start a new job. On your first day, you adjust your chair height, set up your dual monitors, and log into your computer. You do this **once**. The next day, you just sit down and work—the computer "remembers" your preferences.

A configuration file works the same way for software tools like Pytest. It is a plain text file where you write down your preferences (settings) **once**. Every time you run the tool, it reads this file and behaves exactly how you want it to, automatically.

**Why not just type the settings every time?** If you want Pytest to be "verbose" (show detailed output), you could type `pytest -v` every time. But if you have 10 flags you always use, typing them becomes tedious. Worse, if a new developer joins your team, they won't know which flags to use, and their test results will look different from yours.

A configuration file solves this by storing these rules in the project folder. Everyone who downloads the project gets the same settings automatically.

**What Does a Configuration File Look Like?**
Configuration files are deliberately simple. They are plain text — you can open them in Notepad if you want to. They do not contain Python code. They do not contain HTML. They use a minimal, readable format where you write a setting name, an equals sign, and the value you want.
Here is a real configuration file for pytest:
```python
[pytest]
addopts = -v
testpaths = tests
markers =
    slow: marks tests that are slow
    fast: marks tests that are fast
```
A configuration file is not a Python script. It does not get executed line by line. It does not have functions or variables. The tool simply reads it, finds the settings it recognises, and ignores everything else. You cannot break anything by making the file too complex — it has no complexity. It is just a list of instructions written in plain English.


### The Three Things a Configuration File Does

Almost every configuration file in software does exactly three things — no more:

#### Thing 1 — Stores your preferences so you do not have to repeat them

Instead of typing pytest -v --tb=short every time, you write those preferences in the config file once. Every future run picks them up automatically.

#### Thing 2 — Tells the tool about things it does not know yet

Some tools need to be told about things you have created. Pytest, for example, only knows about its own built-in markers. If you invent a new marker called @pytest.mark.slow, pytest has never heard of it. The configuration file is where you formally introduce your new marker to pytest.

#### Thing 3 — Makes behaviour consistent across a whole team

Because the configuration file lives inside the project folder — alongside your code — everyone who works on the project automatically uses the same settings. A new team member clones the project and gets identical behaviour from day one.

**One-Line Definition**

A configuration file is a plain text file that stores settings for a software tool, so that the tool behaves the way you want it to — automatically, every time you use it.

### Configuration Files in the Python World

Python tools use configuration files very widely. You will encounter them throughout your career as a Python developer. Here are the most common ones you will meet, grouped by which tool they belong to:

| File name | Tool it belongs to | What it configures |
| --- | --- | --- |
| pytest.ini | pytest | Registers custom markers, sets default flags, specifies which folder holds tests. |
| pyproject.toml | Many tools | The modern standard. Can hold settings for pytest, Black, Ruff, mypy, and packaging — all in one file. |
| .flake8 | flake8 | Configures the code style checker — which rules to ignore, maximum line length, etc. |
| mypy.ini | mypy | Configures the type checker — how strict to be, which packages to check. |
| setup.cfg | setuptools | Older packaging and tool configuration format. Still common in existing projects. |
| .env | Your application | Stores environment variables — things like API keys, database passwords, feature flags. Never committed to Git. |
| requirements.txt | pip | Lists which Python packages the project depends on. Technically a configuration file for the package installer. |


**You May Have Already Used a Configuration File**

If you have ever used pip install -r requirements.txt, you have already used a configuration file. The requirements.txt file is nothing more than a list of settings (package names and versions) that tells pip what to install. There was no magic — you wrote a list in a file, and a tool read it. All configuration files work on exactly this principle.

#### Flowchart explaining how configuration file is used

![Flocchart explaining how configuration file works](/resources/ch16-pytest-060-config1.png)



### 2. Why Does Pytest Need One?

The most common reason beginners create a configuration file is to fix a specific warning.

#### The "Unknown Marker" Warning

When you learned about markers, you might have written code like this:

```python
import pytest
@pytest.mark.slow # A custom marker we invented
def test_database_backup():
    pass
```
When you run this, Pytest prints a warning:

> `PytestUnknownMarkWarning: Unknown pytest.mark.slow`

**Why?** Pytest knows about its own built-in markers (like `skip`), but it doesn't know about your new marker `slow`. It thinks you might have made a typo.

**The Fix:** You need to "introduce" your marker to Pytest in a configuration file. Once registered, the warning disappears, and you can run commands like `pytest -m slow` to filter your tests correctly.

----------

### 3. The Two Main Files: `pytest.ini` vs `pyproject.toml`

Pytest can read settings from different files, but you only need to pick one. Here is how to choose:

| Feature | pytest.ini | pyproject.toml |
| --- | --- | --- |
| Format | INI (key = value) | TOML (key = value inside sections) |
| Section Header | [pytest] | [tool.pytest.ini_options] |
| Best For | Test-focused projects | Modern Python projects |
| Difficulty | Simplest | Slightly more structured |
| Readability | Very easy for beginners | Slightly more verbose |
| Modernity | Older, traditional approach | Modern Python standard |
| Supports Other Tools | No (pytest only) | Yes (black, ruff, mypy, pytest, etc.) |
| Single Configuration File | No | Yes |
| Suitable for Small Projects | Excellent | Excellent |
| Suitable for Large Projects | Good | Excellent |
| Most Common in New Projects | Less common | More common |
| Learning Recommendation | Start here | Learn after understanding pytest.ini |

### 4. Where Does the File Live?

Your configuration file must live in the **Project Root**. The "Project Root" is the main folder for your project—the folder where you usually type `pytest` in your terminal.

**Structure Example:**

```python
my_project/ <-- Project Root (Put file here)
│
├── pytest.ini <-- The Configuration File
├── src/
│ └── bank_account.py
└── tests/
└── test_bank.py
```

**How Pytest finds it:** When you run `pytest`, it looks at the folder you are currently in. If it doesn't see a config file, it looks in the parent folder, and then the grandparent folder, until it finds one.

#### Flowchart showing how Pytest finds the configuration file

![Flowchart showing how Pytest finds the configuration file](/resources/ch16-pytest-065-config2.png)

----------

### 5. How to Fix the Warning (Step-by-Step)

Let's create a `pytest.ini` file to register the `slow` and `fast` markers.

#### Step 1: Create the file

Create a file named `pytest.ini` in your project root. The first line must be `[pytest]`.

#### Step 2: Add the `markers` section

Under `[pytest]`, add a line starting with `markers =`. List your markers one per line. The format is `name: description`.

```python
[pytest]
markers =
    slow: marks tests as slow (run with: pytest -m slow)
    fast: marks tests as fast unit tests
    db: marks tests that need a database
```
#### Step 3: Run Pytest

Now, run your tests again. The warning is gone!

```python

$ pytest

========================== 2 passed ===========================
```
#### Step 4: Use the markers

Now you can filter your tests:

```python
# Run ONLY slow tests
pytest -m slow
```
  

### Run ONLY fast tests

```python
pytest -m fast
```
  

### Run everything EXCEPT slow tests

```python
pytest -m "not slow"
```
----------

### 6. Useful Tricks: Default Flags (`addopts`)

Aside from markers, the most useful setting is `addopts`. This stands for **"Additional Options."**

If you are tired of typing `pytest -v --tb=short` every single time, you can set it as the default in your config file.

**Example `pytest.ini`:**

```python
[pytest]
# Register markers
markers =
    slow: marks tests as slow

# Set default flags
addopts = -v --tb=short
```
**Result:** Now, if you just type `pytest`, Pytest behaves exactly as if you typed `pytest -v --tb=short`.

----------

### 7. Visualizing the Lifecycle (Flowchart)

![Flowchart](/resources/ch16-pytest-070-config3.png)


### 8. A Complete Worked Example

Here is a full example using the `BankAccount` class.

**File 1: `bank_account.py`** (The Application Code)

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
```


**File 2: `tests/test_bank.py`** (The Tests)

```python
import pytest
from bank_account import BankAccount

@pytest.mark.fast
def test_deposit_small_amount():
    # A fast, in-memory test
    account = BankAccount("Alice", 100)
    account.deposit(50)
    assert account.get_balance() == 150

@pytest.mark.slow
def test_deposit_large_amount():
    # A test that might take longer (simulated)
    import time
    account = BankAccount("Bob", 0)
    time.sleep(0.5)
    account.deposit(1000000)
    assert account.get_balance() == 1000000

```


**File 3: `pytest.ini`** (The Configuration)

```python
[pytest]
addopts = -v
markers =
    fast: Quick unit tests
    slow: Slow integration tests
```
**Scenario 1: Run all tests**

```python
$ pytest

# Output:

# test_bank.py::test_deposit_small_amount PASSED

# test_bank.py::test_deposit_large_amount PASSED
```
**Scenario 2: Run ONLY fast tests (Filtering)**

```python
$ pytest -m fast
# Output:
# test_bank.py::test_deposit_small_amount PASSED
# 1 passed, 1 deselected in 0.02s
```
_Note: The `slow` test was "deselected" (ignored) because of the filter._
**What you want to do**

| do | Command / Code | Notes |
| --- | --- | --- |
| Create the file | pytest.ini | Must start with [pytest] header. |
| Register a marker | slow: description | Goes under markers =. |
| Run fast tests | pytest -m fast | Filters by the marker name. |
| Exclude slow tests | pytest -m "not slow" | Use quotes if using not. |
| List all markers | pytest --markers | Shows what is registered. |
| Default flags | addopts = -v | Saves typing long commands. |
| Verify config | pytest --co -q | Shows configfile: pytest.ini if found. |
