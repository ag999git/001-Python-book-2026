# test_bank_xunit_variations.py
# Trying to give different tests different starting accounts
# while still having only ONE setup_method.

import pytest
from bank_account import BankAccount


class TestAccountTypes:

    # Step 1 - One setup_method has to handle every case
    def setup_method(self, method):
        # Step 2 - Look at the name of the test that is about to run
        name = method.__name__
        # Step 3 - Choose the starting account with if/elif/else
        if name == "test_vip_account":
            self.account = BankAccount("Bruce", 10000)
        elif name == "test_frozen_account":
            self.account = BankAccount("Clark", 500, status="frozen")
        else:
            self.account = BankAccount("John", 100)
        print(f"\n[setup] {name}: owner={self.account.owner}, "
              f"balance={self.account.balance}, status={self.account.status}")

    def test_regular_account(self):
        self.account.deposit(50)
        assert self.account.get_balance() == 150

    def test_vip_account(self):
        self.account.withdraw(1000)
        assert self.account.get_balance() == 9000

    def test_frozen_account(self):
        # A frozen account must refuse a deposit
        with pytest.raises(ValueError):
            self.account.deposit(50)
