





# Exception Testing in pytest — Why `pytest.raises` is better than try/ except

## 1. Introduction

Exception handling is one of the most common areas where beginners write misleading tests. This guide explains why `pytest.raises()` is preferred over manual `try/except` patterns.

----------

## 2. Example Function

```python
def create_user(age):
    if age < 13:        
        raise ValueError("User must be at least 13 years old")    
    return "User created"
```

Business rule:

-   `age < 13` → error
-   `age ≥ 13` → success

----------

## 3. Incorrect Approach (Using only try/except without else)

```python
def test_create_user():
    try:        
        create_user(10)    
    except ValueError:        
        pass
```

### Problem

If the function is broken and stops raising the exception, the test still passes.

#### Flow chart (Using only try/except without else)
![try/except without else](/resources/ch16-pytest-010-only-try-except-no-else.png)


----------

## 4. Improved Manual Approach (try/except/else)

```python
def test_create_user():
    try:        
        create_user(10)    
    except ValueError:        
        pass    
    else:        
        assert False, "Expected ValueError was not raised"
```

### Why this works

-   `except` → handles expected exception
-   `else` → catches missing exception


#### Flow chart for try/except with else

![Flow chart for try/except with else](/resources/ch16-pytest-020-try-except-with-else.png)


----------

## 5. Recommended Approach (`pytest.raises`)

```python
import pytest
def test_create_user():    
    with pytest.raises(ValueError):        
        create_user(10)
```
#### Flow chart of pytest raises

![Flow chart of pytest raises](/resources/ch16-pytest-030-pytest-raises.png)


### Why this is better

-   Clear intention
-   Less boilerplate
-   Automatically fails if exception is missing
-   Easier to read

----------

## 6. Key Insight: Black-box Testing

Tests do NOT inspect internal logic like:

```
if age < 13
```

Instead they verify behavior:

-   Input → Output / Exception

This is called **black-box testing**.

----------

## 7. Common Misunderstanding

WRONG to say → “Test should check if age < 13 exists in code”  
CORRECT to say→ “Test should check behavior for age = 10”

----------

## 8. Valid vs Invalid Inputs

```python
create_user(10)  # should raise error
create_user(14)  # should succeed
```

Each test case checks one observable behavior.

----------

## 9. Internal Working of pytest.raises

Conceptually:

```python
try:    
    create_user(10)
except ValueError:    
    pass
else:    
    raise AssertionError("DID NOT RAISE ValueError")
```

----------

## 10. Summary

-   Tests verify behavior, not implementation
-   Exception tests must fail when exception is missing
-   `pytest.raises()` is the cleanest and safest approach
