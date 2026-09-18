# test_database.py
# The file used for testing database.py.
# Run it with:  pytest -v -s test_database.py

# Step 1 - Import pytest and the class to be tested
import pytest
# The file to be tested is database.py, which contains the Database class.
from database import Database


# Step 2 - The fixture (the dependency provider)
# -----------------------------------------------
# The fixture named 'db' creates a new Database object for each test that requests it.

@pytest.fixture
def db():
    print("\n[FIXTURE] creating database object")
    return Database()


# Step 3 - The tests (the dependency users)
# -----------------------------------------------

# -----------------------------
# TEST 1: Injection Check
# -----------------------------

# The fixture function is named 'db',
# and in test_injection() we are requesting it by including 'db' as a parameter.
# Pytest will create a new Database object by calling the db() fixture function
# and pass it to the test.
# The passing is done by injecting the fixture's return value into the test function's parameter.
# So inside test_injection() the variable name 'db' refers to the Database object created by the fixture.
# So 'db' plays 2 roles:
# 1. It is the name of the fixture function that creates the Database object.
# 2. It is the name of the parameter in the test function that receives the injected Database object.
def test_injection(db):
    print("[TEST 1] test_injection started")
    # This should show <class 'database.Database'> if injection worked correctly.
    print(f"[TEST 1] injected type = {type(db)}")

    # Check that the injected object is an instance of Database
    assert isinstance(db, Database)

    print("[TEST 1] injection successful")


# -----------------------------
# TEST 2: Method Call Check
# -----------------------------
def test_connect(db):
    print("[TEST 2] test_connect started")

    # Call the connect method of the injected Database object
    result = db.connect()
    print(f"[TEST 2] result = {result}")

    # Check that the connect method returns the expected value
    assert result == "connected"

    print("[TEST 2] connect successful")


# -----------------------------
# TEST 3: State Check
# -----------------------------
def test_state(db):
    print("[TEST 3] test_state started")

    # Modify the state of the injected Database object by adding a new attribute
    db.new_flag = "set in test_state"
    print("[TEST 3] modified object state")

    # Check that the state modification is successful
    assert db.new_flag == "set in test_state"

    print("[TEST 3] state modification successful")


# -----------------------------
# TEST 4: Fresh Object Check
# -----------------------------
# test_state() added 'new_flag' to its Database object.
# This test runs after it. If it received the same object,
# 'new_flag' would still be there. It is not, because the fixture
# has the default function scope and creates a new object for every test.
def test_fresh_object(db):
    print("[TEST 4] test_fresh_object started")

    has_flag = hasattr(db, "new_flag")
    print(f"[TEST 4] does this object have new_flag? {has_flag}")

    assert has_flag is False

    print("[TEST 4] each test received its own fresh object")
