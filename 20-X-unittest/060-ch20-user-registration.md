

## Online resource:
It contains a user-registration validation example together with a detailed walkthrough covering:

-   What the script does
-   Why each validation rule exists
-   How the implementation works
-   Exception-handling techniques
-   Testing strategies using pytest.raises()
-   Key software engineering concepts such as input validation, defensive programming, and fail-fast design

Readers are encouraged to study both the source code and the accompanying discussion to gain a deeper understanding of how exception testing is used in real-world applications.


## Folder structure 
It should be something similar to as given below:

```python
ch16-scripts/
│
├── user_registration.py
└── test_user_registration.py

```

##  user_registration.py. This module contains the create_user function that we want to test. 


```python

# user_registration.py
# This module contains the create_user function that we want to test.
import re  # Importing the regular expression module to validate email addresses

def create_user(username, age, email):  # This function creates a user dictionary after validating the input parameters.
    if not username:   # If the username is empty, we raise a ValueError with a specific message.
        raise ValueError("Username cannot be empty")  #

    if age < 13:  # If the age is less than 13, we raise a ValueError with a specific message.
        raise ValueError("User must be at least 13 years old")

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):  # If the email is not valid, we raise a ValueError with a specific message.
        raise ValueError("Invalid email address")

    # If all validations pass, we return a dictionary representing the user.
    return {
        "username": username,
        "age": age,
        "email": email,
    }

```







## test_user_registration.py. This is the file used to test user_registration.py

```python
# test_user_registration.py
# To run the tests in this file, use the command: pytest test_user_registration.py
import pytest
# user_registration.py contains the create_user function that we are testing.
from user_registration import create_user

def test_empty_username():  # Test that creating a user with an empty username raises ValueError
    with pytest.raises(ValueError):  # Test that ValueError is raised when username is empty
        create_user("", 20, "alice@example.com")  # This should raise ValueError because username cannot be empty

def test_username_message():  # Test that the exception message for empty username is correct
    with pytest.raises(
        ValueError,
        match="Username cannot be empty"  # Assert that the exception message contains "Username cannot be empty"
    ):
        create_user("", 20, "alice@example.com")  # This should raise ValueError with the correct message


def test_underage_user():  # Test that creating a user under 13 years old raises ValueError
    with pytest.raises(ValueError) as excinfo:
        create_user("alice", 10, "alice@example.com")

    assert excinfo.type is ValueError  # Assert that the exception type is ValueError
    assert "13 years old" in str(excinfo.value)  # Assert that the exception message contains "13 years old"


def test_invalid_email():  # Test that creating a user with an invalid email raises ValueError
    with pytest.raises(
        ValueError,
        match="Invalid email address"  # Assert that the exception message contains "Invalid email address"
    ):
        create_user("alice", 20, "bad-email")  # This should raise ValueError with the correct message


def test_valid_user():  # Test that creating a valid user returns the correct user dictionary
    user = create_user(
        "alice",
        20,
        "alice@example.com"
    )

    assert user["username"] == "alice"  # Assert that the username in the returned user dictionary is correct
    assert user["age"] == 20  # Assert that the age in the returned user dictionary is correct
    assert user["email"] == "alice@example.com"  # Assert that the email in the returned user dictionary is correct

```


## pytest
The output on following command on terminal:
`pytest -v test_user_registration.py`

### The output is as follows
```python
C:\ch16-scripts> pytest -v test_user_registration.py
========================================== test session starts ===========================================
platform win32 -- Python 3.10.10, pytest-9.0.3, pluggy-1.6.0 -- C:\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\ch16-scripts
plugins: anyio-4.12.1
collected 5 items                                                                                         

test_user_registration.py::test_empty_username PASSED                                               [ 20%]
test_user_registration.py::test_username_message PASSED                                             [ 40%]
test_user_registration.py::test_underage_user PASSED                                                [ 60%]
test_user_registration.py::test_invalid_email PASSED                                                [ 80%]
test_user_registration.py::test_valid_user PASSED                                                   [100%]

=========================================== 5 passed in 0.03s ============================================

```




# Discussion: Testing User Validation with pytest.raises()

## Overview

This example demonstrates how exceptions can be used to enforce validation rules and how those exceptions can be tested using `pytest.raises()`.

The application code contains a small user-registration function called `create_user()`. Before creating a user record, the function validates the supplied information and rejects invalid input by raising exceptions.

Although the example is intentionally small, it mirrors patterns frequently found in production systems, including:

-   Input validation
-   Business-rule enforcement
-   Defensive programming
-   Exception-based error handling
-   Fail-fast design

The example was specifically chosen because it provides several opportunities to demonstrate different ways of testing exceptions with pytest.

## What the Script Does

The purpose of the script is to create a user record.

The function accepts three pieces of information:

```python
username
age
email
```

Before returning a user record, the function verifies that:

1.  A username has been provided.
2.  The user is at least 13 years old.
3.  The email address appears to be valid.

If any of these requirements are violated, the function immediately raises a `ValueError`.

Only valid data is allowed through.



## Need for validation in the Script

Real-world applications constantly receive input from users and external systems.

Examples include:

-   Registration forms
-   Login pages
-   Configuration files
-   APIs
-   Databases

Input cannot be trusted automatically.

Users make mistakes.

Applications therefore validate incoming information before processing it.

This script demonstrates that principle in a simple and approachable form.

----------

## How the Script Works

### Username Validation

```python
if not username:
    raise ValueError("Username cannot be empty")
```

The first validation checks whether a username exists.

Examples that fail:

```python
create_user("", 20, "alice@example.com")
```

```python
create_user(None, 20, "alice@example.com")
```

The function raises an exception because an empty username is not acceptable.

----------

### Age Validation

```python
if age < 13:
    raise ValueError(
        "User must be at least 13 years old"
    )
```

This validation enforces a business rule.

The application has decided that users younger than 13 cannot register.

Example:

```python
create_user("alice", 10, "alice@example.com")
```

Result:

```python
ValueError:
User must be at least 13 years old
```

----------

### Email Validation

```python
if not re.match(
    r"^[^@]+@[^@]+\.[^@]+$",
    email
):
    raise ValueError(
        "Invalid email address"
    )
```

This validation uses a regular expression.

The expression checks that the email roughly follows this pattern:

```python
name@example.com
```

The validation is intentionally simple.

Its purpose is to demonstrate validation logic rather than provide industrial-strength email verification.

----------

### Successful Completion

If all validation checks pass, the function returns a dictionary.

Example:

```python
user = create_user(
    "alice",
    20,
    "alice@example.com"
)
```

Result:

```python
{
    "username": "alice",
    "age": 20,
    "email": "alice@example.com"
}
```

----------

## Why ValueError Is Used

The function raises `ValueError` because the values supplied by the caller are unacceptable.

The arguments themselves are valid parameters.

The problem lies in their contents.

Examples:

```python
""
```

```python
10
```

```python
"not-an-email"
```

This is exactly the situation for which `ValueError` was designed.

----------

## Learning Points

### Input Validation

The script demonstrates how applications verify incoming data before using it.

Validation is one of the most common tasks in software development.

----------

### Defensive Programming

The function assumes that callers may provide invalid data.

Instead of trusting its inputs, it verifies them.

This style is known as `defensive programming`.

----------

### Raising Exceptions

The script shows how exceptions communicate errors.

```python
raise ValueError(...)
```

Rather than returning an error code, the function raises an exception containing meaningful information.

----------

### Fail-Fast Design

Notice that validation stops as soon as a problem is discovered.

For example:

```python
create_user("", 10, "bad-email")
```

The username validation fails first.

The remaining validations never execute.

This is known as fail-fast behavior.

----------

### Business Rules

 - The age requirement is not a Python rule.
 - It is a business rule defined by the application.
 - Many production systems contain hundreds of similar rules.

----------

### Regular Expressions

The script introduces practical regex usage.

Regular expressions are widely used for:

-   Validation
-   Searching
-   Parsing
-   Data extraction
-   Data cleaning

----------

## Why This Example Is Good for `pytest.raises()`

The function contains multiple independent failure paths.

Each path can be tested separately.

Examples include:

-   Empty username
-   Underage user
-   Invalid email address

This allows us to demonstrate several pytest features.

----------

## Testing Exception Occurrence

```python
with pytest.raises(ValueError):
    create_user("", 20, "alice@example.com")
```

This verifies that an exception is raised.

----------

## Testing Exception Messages

```python
with pytest.raises(
    ValueError,
    match="Username cannot be empty"
):
    create_user("", 20, "alice@example.com")
```

This verifies both the exception type and message.

----------

## Using excinfo

```python
with pytest.raises(ValueError) as excinfo:
    create_user("alice", 10, "alice@example.com")
```

The captured exception can then be inspected.

```python
assert excinfo.type is ValueError
```

```python
assert "13 years old" in str(excinfo.value)
```

----------

## Functional Form

Pytest also supports a functional style.

```python
pytest.raises(
    ValueError,
    create_user,
    "",
    20,
    "alice@example.com"
)
```

Although less common today, readers may encounter this form in older codebases.

----------

## Key Takeaways

This small example demonstrates several important software engineering concepts:

-   Input validation
-   Defensive programming
-   Exception handling
-   Fail-fast design
-   Business-rule enforcement
-   Regular-expression matching
-   Unit testing with pytest

More importantly, it shows how `pytest.raises()` can be used to verify that code behaves correctly when invalid input is encountered.
