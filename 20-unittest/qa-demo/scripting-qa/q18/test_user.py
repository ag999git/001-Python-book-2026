# test_user.py
# Run it with:  pytest -v -s test_user.py

import pytest


class User:

    def __init__(self):
        self.name = "Student"


@pytest.fixture
def user():
    # Step 1: Create the common object
    print("\n[FIXTURE] creating user")
    return User()


class TestUser:

    def test_name(self, user):
        # Step 2: The fixture object is injected (after self)
        assert user.name == "Student"

    def test_type(self, user):
        # Step 3: The same fixture is used again
        assert isinstance(user, User)
