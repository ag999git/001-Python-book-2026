# test_session_fixture.py
# Run it with:  pytest -v -s test_session_fixture.py

import pytest


class Database:

    def connect(self):
        print("[DB] connecting")
        return "connected"


# Step 1: Create a session-scoped fixture
@pytest.fixture(scope="session")
def db():
    print("\n[FIXTURE] session setup")

    # Step 2: Create the object once, and connect once
    database = Database()
    database.connect()

    # Step 3: Provide the same object to all tests
    yield database

    # Step 4: Runs once, after all tests have finished
    print("\n[FIXTURE] session teardown")


def test_one(db):
    print("[TEST] one")
    assert isinstance(db, Database)


def test_two(db):
    print("[TEST] two")
    assert isinstance(db, Database)


def test_three(db):
    print("[TEST] three")
    assert db.connect() == "connected"
