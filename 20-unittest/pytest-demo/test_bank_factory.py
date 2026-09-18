# test_bank_factory.py
# A "factory" fixture: instead of one ready-made account,
# the fixture returns a function that can build any account we ask for.

# Step 1 - Import pytest and the class under test
import pytest
from bank_account import BankAccount


# Step 2 - The factory fixture
@pytest.fixture
def make_account():
    """Return a function that creates a BankAccount with any settings."""

    def _make(owner="John", balance=100, status="active"):
        print(f"\n[factory] owner={owner}, balance={balance}, status={status}")
        return BankAccount(owner, balance, status)

    return _make


# Step 3 - Each test builds exactly the account it needs
def test_regular(make_account):
    account = make_account()
    account.deposit(50)
    assert account.get_balance() == 150


def test_vip(make_account):
    account = make_account("Bruce", 10000)
    account.withdraw(1000)
    assert account.get_balance() == 9000


def test_frozen(make_account):
    account = make_account("Clark", 500, status="frozen")
    with pytest.raises(ValueError):
        account.withdraw(100)
    assert account.get_balance() == 500
