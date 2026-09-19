# calculator.py
# Small functions used by the demo tests on this page.


def square(number):
    return number * number


def add(a, b):
    return a + b


def add_buggy(a, b):
    # A deliberate bug, used to show pytest's failure messages
    return a + b + 1


def set_age(age):
    if age < 0:
        raise ValueError("invalid age: age cannot be negative")
    return age
