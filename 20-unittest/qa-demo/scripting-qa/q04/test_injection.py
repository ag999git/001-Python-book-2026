# test_injection.py
# Run it with:  pytest -v -s test_injection.py

import pytest


class User:

    def __init__(self):
        self.name = "Alex"


# Step 1: The fixture function creates a User object
@pytest.fixture
def user():
    print("\n[FIXTURE] creating User object")
    return User()


# Step 2: The test requests "user".
#         pytest finds the fixture named user,
#         calls it, and injects the returned object.
def test_user_injection(user):
    print("[TEST] received object")
    print(type(user))

    # Step 3: Verify the injected object
    assert user.name == "Alex"
