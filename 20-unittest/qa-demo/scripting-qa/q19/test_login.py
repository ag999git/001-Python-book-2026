# test_login.py
# Run it with:  pytest -v -s test_login.py

import pytest


class LoginSystem:

    def check(self, username):
        # Step 1: Simple validation
        if username == "admin":
            return True
        return False


@pytest.fixture
def login():
    # Step 2: Create the object (runs again for EVERY test case)
    print("\n[FIXTURE] creating LoginSystem")
    return LoginSystem()


@pytest.mark.parametrize(
    "username, expected",
    [
        ("admin", True),
        ("guest", False),
        ("abc", False),
    ],
)
def test_login(login, username, expected):

    # Step 3: A fresh fixture object, with a different input each time
    result = login.check(username)
    print(f"[TEST] check({username!r}) -> {result}")

    # Step 4: Check the result
    assert result == expected
