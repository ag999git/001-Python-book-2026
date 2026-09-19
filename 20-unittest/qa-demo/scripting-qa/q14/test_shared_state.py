# test_shared_state.py
# Run it with:  pytest -v -s test_shared_state.py

import pytest


class User:

    def __init__(self):
        self.logged_in = False


@pytest.fixture(scope="session")
def user():

    # Step 1: Create one shared object
    print("\n[FIXTURE] creating user")
    return User()


def test_login(user):

    # Step 2: Change the shared object
    user.logged_in = True
    print("[TEST] user logged in")
    assert user.logged_in == True


def test_status(user):

    # Step 3: This test receives the SAME object
    print(f"[TEST] checking status: logged_in = {user.logged_in}")
    assert user.logged_in == True
