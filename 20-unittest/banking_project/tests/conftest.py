# File: tests/conftest.py
# Description: Shared fixture repository for every test file in the tests
# folder and in all the folders inside it. Do not put test functions here.
# Pytest finds this file by its name. No test file ever imports it.

# Step 1 - Import pytest and the class the fixture will build
import pytest
from bank_account import BankAccount


# Step 2 - The shared fixture
@pytest.fixture
def fresh_account():
    """A new BankAccount for John with a balance of 100, created fresh for every test."""

    # --- SETUP (runs before each test that asks for fresh_account) ---
    print("\n[CONFTEST FIXTURE] Creating fresh account for a distributed test...")
    account_instance = BankAccount("John", 100)

    # Hand the account to whichever test asked for it
    yield account_instance

    # --- TEARDOWN (runs after that test has finished) ---
    print("\n[CONFTEST FIXTURE] Tearing down account after the test...")
