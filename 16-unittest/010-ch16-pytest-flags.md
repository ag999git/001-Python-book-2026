



# Understanding Pytest Command-Line Flags

Pytest provides many command-line options that control how tests are executed and how results are displayed. The accompanying online resource explores three of the most frequently used flags: `-v` (verbose output), `-s` (show print statements), and `-k` (run selected tests by name). Through detailed examples, output comparisons, practical debugging scenarios, summary tables, and visual flowcharts, the resource demonstrates how these flags can significantly improve productivity while developing and debugging test suites.

 Mastering a few commonly used flags can greatly improve the testing experience and make pytest much easier to use in real-world projects.

## Table of Contents

* [Introduction](010-ch16-pytest-flags.md#introduction)
* [Mental Model](010-ch16-pytest-flags.md#mental-model)
* [How Pytest Processes Flags](010-ch16-pytest-flags.md#how-pytest-processes-flags)
* [The -v Flag (Verbose Mode)](010-ch16-pytest-flags.md#the--v-flag-verbose-mode)
* [The -s Flag (Show print() Output)](010-ch16-pytest-flags.md#the--s-flag-show-print-output)
* [Why Does Pytest Hide print() Output?](010-ch16-pytest-flags.md#why-does-pytest-hide-print-output)
* [The -k Flag (Test Selection)](010-ch16-pytest-flags.md#the--k-flag-test-selection)
* [Combining Flags](010-ch16-pytest-flags.md#combining-flags)
* [Typical Pytest Workflow](010-ch16-pytest-flags.md#typical-pytest-workflow)



# Understanding Common Pytest Command-Line Flags

## Introduction

As test suites grow larger, running every test every time can become slow and inefficient. Pytest provides a rich collection of command-line flags that allow us to control how tests are executed and how results are displayed.

This resource focuses on three of the most frequently used pytest flags:

-   `-v` : Verbose mode
-   `-s` : Show output from `print()` statements
-   `-k` : Select tests by name

Although these flags are simple, they are used extensively in real-world development and debugging.

----------

## Mental Model

Think of these flags as controlling different aspects of pytest.

| Flag | Controls |
| --- | --- |
| -v | How much detail is displayed |
| -s | Whether print() output is visible |
| -k | Which tests are executed |


### Visual Representation

![Visual Representation](/resources/ch16-pytest-080-flags-mental-model.png)


### Important Terminology


| Term | Meaning |
| --- | --- |
| Verbose | Display more detailed information |
| Output Capture | Pytest temporarily hides print() output |
| Selected | Tests chosen for execution |
| Deselected | Tests skipped by a selection filter such as -k |
| Collected | Tests discovered by pytest during test discovery |
| Pattern Matching | Finding names that contain specified text |


### How Pytest Processes Flags

When pytest starts, it first discovers tests and then applies any command-line flags supplied by the user.

![How pytest processes flags](/resources/ch16-pytest-090-how-process-flags.png)


[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)

## The -v Flag (Verbose Mode)

### Purpose

The `-v` flag tells pytest to display detailed information about each test that is executed.

**Without `-v`, pytest displays a compact progress line using dots.**

Example:

```python
pytest
```

Output:

```python
3 passed
```

**With verbose mode:**

```python
pytest -v
```

**Output:**

```python
test_addition      PASSED
test_subtraction   PASSED
test_multiply      PASSED
```

----------

### Why Use -v ?

-   Shows individual test names
-   Easier debugging
-   Useful when many tests exist
-   Helps identify failing tests quickly

----------

### Example Script

```python
def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 10 - 3 == 7

def test_multiplication():
    assert 3 * 4 == 12
```

Run:

```python
pytest -v
```
### The output is

```python
================================================== test session starts ==================================================
platform win32 -- Python 3.10.10, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Anurag Gupta\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\One-Drive-2025\OneDrive\Harmonica
plugins: anyio-4.12.1
collected 3 items                                                                                                        

test1112.py::test_addition PASSED                                                                                  [ 33%]
test1112.py::test_subtraction PASSED                                                                               [ 66%]
test1112.py::test_multiplication PASSED                                                                            [100%]

=================================================== 3 passed in 0.02s ===================================================
```

----------
[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)

## The -s Flag (Show `print()` Output)

### Purpose

**By default, pytest captures and does not display output produced by `print()` statements.**

This keeps test reports clean.

Example:

```python
def test_demo():
    print("Hello")
    assert True
```

**Run (Without -s flag):**

```python
pytest
```

Output:

```python
1 passed
```

Notice that:

```python
Hello
```

is not displayed.

----------

### Run Using -s flag

Run:

```python
pytest -s
```

Output:

```python
Hello
1 passed
```

Now the output is visible.

----------
[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)

## Why Does Pytest Hide `print()` Output?

Pytest uses a mechanism called **output capture**.

Output capture collects printed text and hides it unless the test fails or the user explicitly requests it.

### Output Capture Flow

![Output Capture Flow](/resources/ch16-pytest-092-flags-output-capture.png)


### Why Use -s ?

-   Debugging
-   Viewing intermediate values
-   Understanding program flow
-   Learning and experimentation

----------

### Example

```python
def test_balance():
    balance = 100
    print("Initial Balance:", balance)
    balance += 50
    print("Updated Balance:", balance)
    assert balance == 150
```

Run: (with -s flag)

```
pytest -s
```
### Output is:

```python
================================================== test session starts ==================================================
platform win32 -- Python 3.10.10, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Anurag Gupta\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\One-Drive-2025\OneDrive\Harmonica
plugins: anyio-4.12.1
collected 1 item                                                                                                         

test1112.py::test_balance PASSED                                                                                   [100%]

=================================================== 1 passed in 0.02s ===================================================
```


----------

[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)

## The -k Flag (Test Selection)

### Purpose

The `-k` flag allows pytest to execute only tests whose names match a specified pattern.

Example:

```python
pytest -k deposit
```

Only tests containing:

```python
deposit
```

in their names are executed.

----------

## Example Script

```python
# test_bank.py
def  test_deposit():
    print("Running deposit test")
    balance = 100
    balance += 50
    assert  balance == 150

def  test_withdraw():
    print("Running withdraw test")
    balance = 100
    balance -= 30
    assert  balance == 70

def  test_deposit_large_amount():
    print("Running large deposit test")
    balance = 100
    balance += 1000
    assert  balance == 1100
```

Run:

```python
pytest test_bank.py -k deposit -s -v  
```
Note the format:- 
  -  First term is `pytest`
  - Followed by `test_bank.py` which is the name of the file containing the tests
  - Then `-k` flag
  - Then the word "`deposit`" which is used to select tests containing the term/ word "`deposit`"
  - Then finally flags `-s` and `-v`
#### The output is

```python
================================================== test session starts ==================================================
platform win32 -- Python 3.10.10, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Anurag Gupta\AppData\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\
plugins: anyio-4.12.1
collected 3 items / 1 deselected / 2 selected                                                                            

test1112.py::test_deposit Running deposit test
PASSED
test1112.py::test_deposit_large_amount Running large deposit test
PASSED

============================================ 2 passed, 1 deselected in 0.14s ============================================

```


Note that Pytest executes:

```python
test_deposit
test_deposit_large_amount
```

and skips:

```python
test_withdraw
```

----------

[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)


## How -k Works

![How -k works](/resources/ch16-pytest-095-flag-k.png)


## Why Use -k ?

-   Run only a specific test
-   Run a subset of tests
-   Faster debugging
-   Useful in large projects

----------

# Combining Flags

Flags can be combined.
Example:

```python
pytest -v -s -k deposit
```

Meaning:
| Flag | Purpose |
| --- | --- |
| -v | Show test names |
| -s | Show print output |
| -k deposit | Run only deposit tests |

### Combined Execution Flow

![Combined Execution Flow](/resources/ch16-pytest-096-combining-tests.png)


### Common Development Scenarios

| Situation | Recommended Command |
| --- | --- |
| Run all tests | pytest |
| See individual test names | pytest -v |
| View print() output | pytest -s |
| Run one group of tests | pytest -k deposit |
| Debug one test | pytest -v -s -k deposit |
| Debug a failing test | pytest -v -s |

[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)

### Common Beginner Mistakes

#### Mistakes with -v

| Mistake | Reality |
| --- | --- |
| -v changes test behavior | It only changes output detail |
| -v makes tests faster | It only affects display |

Mistakes with -s

| Mistake | Reality |
| --- | --- |
| print() is broken | Pytest is capturing output |
| -s changes test logic | It only changes visibility |


### Mistakes with -k

| Mistake | Reality |
| --- | --- |
| -k filters markers | It filters test names |
| -k slow is same as -m slow | They are different |
| Deselected tests failed | Deselected means not executed |


### Comparison of the Three Flags

| Flag | Purpose | Affects Execution? | Affects Output? | Common During Development? |
| --- | --- | --- | --- | --- |
| -v | Verbose output | No | Yes | Very Common |
| -s | Show print output | No | Yes | Common |
| -k | Select tests by name | Yes | Indirectly | Very Common |


# Typical Pytest Workflow

A common workflow during development is:

```python
1. Write a test
2. Run pytest
3. Observe failure
4. Add print() statements
5. Run pytest -s
6. Run pytest -v
7. Run pytest -v -s -k test_name
8. Fix the bug
9. Run the full test suite
```

[Back to the Table of Contents](010-ch16-pytest-flags.md#table-of-contents)















