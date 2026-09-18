# test_name_mismatch.py
# What happens when the parameter name does NOT match any fixture name?
# Run it with:  pytest -v test_name_mismatch.py
# This test ERRORS on purpose.

# Step 1 - Import pytest and the class to be tested
import pytest
from database import Database


# Step 2 - The fixture is called 'db'
@pytest.fixture
def db():
    return Database()


# Step 3 - The test asks for 'database', which is not the name of any fixture
def test_wrong_name(database):
    assert isinstance(database, Database)
