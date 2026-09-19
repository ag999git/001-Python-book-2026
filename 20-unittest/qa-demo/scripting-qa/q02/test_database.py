# test_database.py
# Run it with:  pytest -v -s test_database.py

import pytest

from database import Database


# Step 1: Create a fixture.
#         The fixture creates the dependency object.
@pytest.fixture
def db():
    print("\n[FIXTURE] creating Database object")

    # Step 2: Create the Database object
    database = Database()

    # Step 3: Return the object to the test
    return database


# Step 4: pytest sees the parameter db.
#         It automatically calls the fixture named db,
#         and the returned Database object is injected here.
def test_connection(db):
    print("[TEST] test_connection")
    result = db.connect()
    assert result == "connected"


# Step 5: A second test receives its own Database object from the same fixture
def test_object_type(db):
    print("[TEST] test_object_type")
    assert isinstance(db, Database)
