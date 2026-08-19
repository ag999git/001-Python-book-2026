



# Project Title: The “Micro-Precision” Tax Calculator (Using Parameterized Testing)


# 1. Problem Statement

You are building a simple Point of Sale system.

The system calculates tax using:

> Tax rate = 10%

Your task is to test the function using multiple inputs efficiently using **parameterized testing**.

----------

# 2. Application script (which is to be tested)

```python
# tax_calculator.py
def calculate_tax(price):    
    tax_rate = 0.10    
    return price * tax_rate
```

----------

# 3. First Attempt — Repetitive Tests - Not using Parameterized Testing (Bad Practice)

```python
# test_tax_calculator.py
from  tax_calculator  import  calculate_tax  # Importing the calculate_tax function from the tax_calculator module to test it.

def  test_tax_1(): # Test case 1: Testing calculate_tax with a price of 1.00
    assert  calculate_tax(1.00) == 0.10  # The expected tax for a price of 1.00 should be 0.10 (10% of 1.00)

def  test_tax_2(): # Test case 2: Testing calculate_tax with a price of 1.10
    assert  calculate_tax(1.10) == 0.11  # The expected tax for a price of 1.10 should be 0.11 (10% of 1.10)

def  test_tax_3(): # Test case 3: Testing calculate_tax with a price of 2.00
    assert  calculate_tax(2.00) == 0.20  # The expected tax for a price of 2.00 should be 0.20 (10% of 2.00)

```


### The output on giving following command on terminal:
`pytest -v test_calculate_tax.py` is as follows

```python
C:\ch16-scripts> pytest -v test_tax_calculator.py
========================================== test session starts ===========================================
platform win32 -- Python 3.10.10, pytest-9.0.3, pluggy-1.6.0 -- C:\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\ch16-scripts
plugins: anyio-4.12.1
collected 3 items                                                                                         

test_tax_calculator.py::test_tax_1 PASSED                                                           [ 33%]
test_tax_calculator.py::test_tax_2 FAILED                                                           [ 66%]
test_tax_calculator.py::test_tax_3 PASSED                                                           [100%]

================================================ FAILURES ================================================
_______________________________________________ test_tax_2 _______________________________________________

    def test_tax_2():
>       assert calculate_tax(1.10) == 0.11
E       assert 0.11000000000000001 == 0.11
E        +  where 0.11000000000000001 = calculate_tax(1.1)

test_tax_calculator.py:8: AssertionError
======================================== short test summary info =========================================
FAILED test_tax_calculator.py::test_tax_2 - assert 0.11000000000000001 == 0.11
====================================== 1 failed, 2 passed in 0.21s =======================================
C:\One-Drive-2025\OneDrive\Python-book-new-2026-NOIDA\016-New-chapter-unit-test-developing-test-suite\ch16-scripts> 


```

## Problem:

-   repetitive code
-   not scalable
-   hard to maintain
-   1 test failed 2 passed (Due to approximation issue- may not be obvious without the test)

----------

# 4. Solution — Parameterized Testing

```python
# test_tax_calculator2.py
# This file contains tests for the calculate_tax function in tax_calculator.py.
# To run the tests in this file, use the command: pytest test_tax_calculator2.py
import  pytest

from  tax_calculator  import  calculate_tax

# We use @pytest.mark.parametrize to run the same test with multiple sets of data.
# "price, expected" are the arguments the test function accepts.
# The list of tuples contains the data sets: (Input, ExpectedResult)
@pytest.mark.parametrize("price, expected", [
(1.00, 0.10),
(1.10, 0.11),
(2.00, 0.20),
(5.50, 0.55),
(10.00, 1.00)
])

def  test_tax_values(price, expected):
    assert  calculate_tax(price) == expected
```

Problem
-  It solves the problem of repetitive code
-  But does not solve the problem of approximation


----------

# 5. What pytest does internally

Each tuple becomes a separate test execution:

| Input (price) | Expected | Test Run |
| --- | --- | --- |
| 1 | 0.1 | Test 1 |
| 1.1 | 0.11 | Test 2 |
| 2 | 0.2 | Test 3 |
| 5.5 | 0.55 | Test 4 |
| 10 | 1 | Test 5 |

# 6. Hidden Problem (Floating Point Issue)

One of these may fail:

```python
assert 0.11000000000000001 == 0.11
```


# 7. Concept Insight

Floating-point numbers are stored approximately in binary.

So:

-   0.1 is not exactly 0.1 internally
-   small precision errors accumulate

----------

# 8. Solution — `pytest.approx` inside parametrize

```python
# test_tax_calculator3.py
# This file contains tests for the calculate_tax function in tax_calculator.py.
# To run the tests in this file, use the command: pytest test_tax_calculator3.py

import  pytest
from  tax_calculator  import  calculate_tax

@pytest.mark.parametrize("price, expected", [
(1.00, 0.10),
(1.10, 0.11),
(2.00, 0.20),
(5.50, 0.55),
(10.00, 1.00)
])

def  test_tax_values(price, expected):
    # We use pytest.approx to compare floating-point numbers,
    # which allows for a small tolerance in the comparison.
    assert  calculate_tax(price) ==  pytest.approx(expected)

```

Here the problem of approximation solved by using `pytest.approx()`


----------

# 9. Flowchart — Parametrized Testing + Execution

![Flowchart — Parametrized Testing + Execution](/resources/ch16-pytest-040-project-tax-collector.png)


## Flowchart here


# 10. Tests are seperate

>Each parameter set becomes a SEPARATE test case.

So:

-   one failure does NOT stop others
-   all inputs are evaluated independently

----------

# 11.  Using `ids` in parametrize

> You can improve readability using `ids` in parametrize:

```python
@pytest.mark.parametrize(
"price, expected",
[
(1.00, 0.10),
(1.10, 0.11),
],
ids=["basic price", "rounded price"] # Custom identifiers for each test case
)
```

This makes test reports much easier to understand.
