# test_fixture_name.py
# The fixture's NAME must match the parameter, but the Python function
# can have a different name if we use the 'name' argument.
# Run it with:  pytest -v -s test_fixture_name.py

# Step 1 - Import pytest and the class to be tested
import pytest
from database import Database


# Step 2 - The function is called make_database, but the fixture's
#          name is 'db', because of name="db"
@pytest.fixture(name="db")
def make_database():
    print("\n[FIXTURE] make_database() running as fixture 'db'")
    return Database()


# Step 3 - The test asks for 'db' (the fixture name), not 'make_database'
def test_uses_fixture_name(db):
    print("[TEST] received:", type(db).__name__)
    assert isinstance(db, Database)
