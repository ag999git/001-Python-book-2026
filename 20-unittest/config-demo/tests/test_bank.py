# tests/test_bank.py
# Tests for bank_account.py, labelled with the custom markers
# 'fast' and 'slow' that are registered in pytest.ini.

# Step 1 - Imports
import time

import pytest
from bank_account import BankAccount


# Step 2 - A quick test, labelled 'fast'
@pytest.mark.fast
def test_deposit_small_amount():
    # A fast, in-memory test
    account = BankAccount("Alice", 100)
    account.deposit(50)
    assert account.get_balance() == 150


# Step 3 - A test that takes longer, labelled 'slow'
@pytest.mark.slow
def test_deposit_large_amount():
    # time.sleep(0.5) pauses for half a second to imitate a slow test
    account = BankAccount("Bob", 0)
    time.sleep(0.5)
    account.deposit(1000000)
    assert account.get_balance() == 1000000
