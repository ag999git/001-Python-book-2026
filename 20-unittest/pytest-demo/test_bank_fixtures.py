# test_bank_fixtures.py
# The same kind of tests, written as plain functions that use pytest fixtures.

# Step 1 - Import pytest and the code we want to test
import pytest
from bank_account import BankAccount, format_currency


# Step 2 - Define the fixtures
#
# A fixture is a function that prepares data or objects
# needed by one or more tests.
# Think of a fixture as a "setup service".
# Instead of creating BankAccount objects inside every test,
# we write the setup code once, in a fixture, and let pytest
# provide the object to the tests that need it.
# By default, pytest runs the fixture again for every test that
# asks for it, so each test gets its own fresh object.
# The code before the yield statement performs SETUP.
# The code after the yield statement performs CLEANUP (teardown).

@pytest.fixture
def regular_account():
    """
    Create a regular bank account for testing.

    Initial state:
        Customer : John
        Balance  : 100
        Status   : active

    Pytest runs the code before 'yield' before the test starts,
    and the code after 'yield' after the test finishes.
    """
    print("\n[setup] regular_account created")
    account = BankAccount("John", 100)

    # Give the account object to the test function.
    yield account

    # Any cleanup code goes here. It runs after the test finishes,
    # even if the test fails. A BankAccount needs no real cleanup,
    # so we only print a message.
    print("\n[teardown] regular_account finished")


@pytest.fixture
def vip_account():
    """
    Create a VIP account for testing.

    Initial state:
        Customer : Bruce
        Balance  : 10000
        Status   : active

    Each test that asks for it gets its own fresh VIP account.
    """
    print("\n[setup] vip_account created")
    account = BankAccount("Bruce", 10000)
    yield account
    print("\n[teardown] vip_account finished")


@pytest.fixture
def frozen_account():
    """
    Create a frozen account for testing.

    Initial state:
        Customer : Clark
        Balance  : 500
        Status   : frozen
    """
    print("\n[setup] frozen_account created")
    account = BankAccount("Clark", 500, status="frozen")
    yield account
    print("\n[teardown] frozen_account finished")


# Step 3 - Write the test functions
#
# Notice that the test functions do NOT create
# BankAccount objects themselves.
# Instead, they simply ask for the fixture by name.
# Pytest sees the fixture name in the function's parameter
# list and automatically calls the fixture.
# This mechanism is called Dependency Injection.

def test_regular_deposit(regular_account):
    """
    Test that money can be deposited into a regular account.
    Pytest automatically supplies the 'regular_account' fixture.
    """
    regular_account.deposit(50)
    print("Regular balance after deposit:", regular_account.get_balance())
    assert regular_account.get_balance() == 150


def test_vip_withdrawal(vip_account):
    """
    Test that money can be withdrawn from a VIP account.
    Pytest automatically supplies the 'vip_account' fixture.
    """
    vip_account.withdraw(1000)
    print("VIP balance after withdrawal:", vip_account.get_balance())
    assert vip_account.get_balance() == 9000


def test_frozen_account_refuses_deposit(frozen_account):
    """
    Test that a frozen account refuses a deposit.
    Pytest automatically supplies the 'frozen_account' fixture.
    """
    # pytest.raises checks that the code inside the 'with' block
    # raises the given error. If it does, this part of the test passes.
    with pytest.raises(ValueError):
        frozen_account.deposit(50)
    print("Frozen account refused the deposit. Balance is still",
          frozen_account.get_balance())
    assert frozen_account.get_balance() == 500


def test_format_currency():
    """
    This test does not need a BankAccount object.

    Since no fixture is requested, pytest does not run
    any fixture setup or cleanup code.
    The test runs completely on its own.
    """
    result = format_currency(1500)
    print("\nFormatted amount:", result)
    assert result == "Rs. 1,500.00"
