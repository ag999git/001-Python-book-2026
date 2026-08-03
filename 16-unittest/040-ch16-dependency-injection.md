

# Dependency Injection in Pytest Fixtures

## Table of Contents
* [Research Question](040-ch16-dependency-injection.md#research-question)
* [Practical Example](040-ch16-dependency-injection.md#practical-example)
* [Further discussion](040-ch16-dependency-injection.md#further-discussion)
* [Flow for EACH test (test_injection / test_connect / test_state)](040-ch16-dependency-injection.md#flow-for-each-test-test_injection--test_connect--test_state)
* [SAME FLOW applies to all 3 tests](040-ch16-dependency-injection.md#same-flow-applies-to-all-3-tests)

## Research Question

What is **dependency injection**, and how does pytest use fixtures to automatically provide objects to test functions?

In traditional programming, objects like database connections or services are created manually inside functions or passed explicitly as arguments. This can lead to repetitive code and tight coupling between test logic and setup logic.

Research and explain:

1.  What is dependency injection in general programming?
2.  Why is it useful in testing?
3.  How does pytest implement dependency injection using `@pytest.fixture`?
4.  Why does the fixture function name need to match the test function parameter name?
5.  How does this mechanism help simplify test writing?

Then, analyze the following code and explain how dependency injection is happening step by step.

----------

## Practical Example

#### database.py
The file which is to be tested

```python

# database.py
# This is a simple database module that simulates connecting to a database.
class Database:
    def __init__(self):
        print("[DB] Database object created")

    def connect(self):  # simulates an expensive connection setup
        print("[DB] connect called")
        return "connected"

```

#### test_database.py
The file used for testing database.py

```python
# test_database.py
import pytest
# The file to be tested is database.py, which contains the Database class.
from database import Database

# Fixture (Dependency Provider)
# -----------------------------
# The fixture named 'db' creates a new Database object for each test that requests it.

@pytest.fixture
def db():
    print("\n[FIXTURE] creating database object")
    return Database()

# -----------------------------
# TEST 1: Injection Check
# -----------------------------

# The fixture function  is named 'db', 
# in test_injection() we are requesting it by including 'db' as a parameter.
# Now pytest will create a new Database object by calling the db() fixture function 
# and pass it to the test.
# The passing is done by injecting the fixture's return value into the test function's parameter.
# So inside test_injection() the variable name 'db' refers to the Database object created by the fixture.
# So 'db' plays 2 roles:
# 1. It is the name of the fixture function that creates the Database object.
# 2. It is the name of the parameter in the test function that receives the injected Database object.
def test_injection(db):
    print("[TEST 1] test_injection started")
    print(f"[TEST 1] injected type = {type(db)}")  # This should show <class 'database.Database'> if injection worked correctly.

    assert isinstance(db, Database)  # Check if the injected object is an instance of Database

    print("[TEST 1] injection successful")

# -----------------------------
# TEST 2: Method Call Check
# -----------------------------
def test_connect(db):
    print("\n[TEST 2] test_connect started")

    result = db.connect()  # Call the connect method of the injected Database object
    print(f"[TEST 2] result = {result}")

    assert result == "connected"  # Check if the connect method returns the expected value

    print("[TEST 2] connect successful")


# -----------------------------
# TEST 3: State Check
# -----------------------------
def test_state(db):
    print("\n[TEST 3] test_state started")

    db.new_flag = "set in test_state"  # Modify the state of the injected Database object
    print("[TEST 3] modified object state")

    assert db.new_flag == "set in test_state"  # Check if the state modification is successful

    print("[TEST 3] state modification successful")

```

## Further discussion



### 1. What is Dependency Injection?

Dependency Injection is a design pattern where an object (dependency) is created outside a function and provided to it automatically or externally instead of being created inside the function.

This helps:

-   reduce repeated setup code
-   improve test readability
-   separate creation logic from usage logic

----------

### 2. How pytest uses dependency injection

In pytest, dependency injection happens through **fixtures**.

When a test function declares a parameter:

```
def test_one(db):
```

pytest performs the following steps:

1.  It sees the parameter name `db`
2.  It looks for a fixture with the same name `db`
3.  It executes the fixture function
4.  It receives the returned object
5.  It injects that object into the test function parameter

### Flow for EACH test (test_injection / test_connect / test_state)

```python
test_injection(db)
        ↓
pytest starts executing test_injection
        ↓
pytest detects parameter name: "db"
        ↓
pytest searches for a fixture named "db"
        ↓
finds:

    @pytest.fixture
    def db():
        return Database()

        ↓
pytest calls db() fixture function
        ↓
inside fixture:
    Database() object is created
        ↓
fixture returns Database object
        ↓
pytest injects returned object into test_injection(db)
        ↓
NOW inside test_injection:
    db → refers to Database object
        ↓
test code executes:
    - type(db)
    - isinstance check
        ↓
test completes


```


### SAME FLOW applies to all 3 tests

```python
test_connect(db)
        ↓
pytest sees "db" parameter
        ↓
find db fixture
        ↓
call db()
        ↓
create Database object
        ↓
return Database object
        ↓
inject into test_connect(db)
        ↓
run:
    db.connect()
        ↓
assert result == "connected"


```



### For test_state(db):

```python
test_state(db)
        ↓
pytest sees "db"
        ↓
find db fixture
        ↓
call db()
        ↓
create Database object
        ↓
return Database object
        ↓
inject into test_state(db)
        ↓
run:
    db.new_flag = "set in test_state"
        ↓
assert db.new_flag


```


















