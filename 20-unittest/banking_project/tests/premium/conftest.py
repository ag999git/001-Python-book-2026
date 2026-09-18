# File: tests/premium/conftest.py
# A second conftest.py, one level deeper. Its fixtures are visible ONLY to
# tests inside the premium folder (and folders below it).

# Step 1 - Import pytest and the class the fixture will build
import pytest
from bank_account import BankAccount


# Step 2 - A fixture that only premium tests can use
@pytest.fixture
def premium_account():
    print("\n[PREMIUM CONFTEST] Creating premium account with balance 10000...")
    return BankAccount("Bruce", 10000)
