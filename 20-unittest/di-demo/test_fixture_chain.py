# test_fixture_chain.py
# A fixture can ask for another fixture, in exactly the same way
# a test does. Pytest builds the whole chain automatically.
# Run it with:  pytest -v -s test_fixture_chain.py

# Step 1 - Import pytest and the class to be tested
import pytest
from database import Database


# Step 2 - First fixture: creates the Database object
@pytest.fixture
def db():
    print("\n[FIXTURE db] creating database object")
    return Database()


# Step 3 - Second fixture: asks for 'db', connects it, and returns both
@pytest.fixture
def connected_db(db):
    print("[FIXTURE connected_db] received db, now connecting")
    status = db.connect()
    return db, status


# Step 4 - The test asks only for 'connected_db'.
#          Pytest sees that connected_db needs db, so it runs db first.
def test_ready_to_use(connected_db):
    database, status = connected_db
    print(f"[TEST] status = {status}")
    assert status == "connected"
    assert isinstance(database, Database)
