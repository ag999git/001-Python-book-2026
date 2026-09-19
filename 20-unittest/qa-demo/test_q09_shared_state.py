# test_q09_shared_state.py - Questions 8 and 9: function vs session scope
# Run it with:  pytest -v -s test_q09_shared_state.py
# One test FAILS on purpose, to show the danger of shared state.

import pytest


class Account:
    def __init__(self):
        self.balance = 100


# Step 1 - A function-scoped fixture: a new Account for every test
@pytest.fixture
def fresh_account():
    return Account()


# Step 2 - A session-scoped fixture: ONE Account shared by all tests
@pytest.fixture(scope="session")
def shared_account():
    return Account()


# Step 3 - Function scope: the change in test A does not reach test B
def test_a_fresh(fresh_account):
    fresh_account.balance = 0
    print(f"\n   test_a_fresh set balance to {fresh_account.balance}")


def test_b_fresh(fresh_account):
    print(f"\n   test_b_fresh received balance {fresh_account.balance}")
    assert fresh_account.balance == 100


# Step 4 - Session scope: the change in test C DOES reach test D
def test_c_shared(shared_account):
    shared_account.balance = 0
    print(f"\n   test_c_shared set balance to {shared_account.balance}")


def test_d_shared(shared_account):
    print(f"\n   test_d_shared received balance {shared_account.balance}")
    assert shared_account.balance == 100
