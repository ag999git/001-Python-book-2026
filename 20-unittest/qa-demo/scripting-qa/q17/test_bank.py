# test_bank.py
# Run it with:  pytest -v test_bank.py

# Step 1: Import both functions
from bank import deposit, withdraw


def test_deposit():
    # Step 2: Test deposit
    result = deposit(100, 50)
    assert result == 150


def test_withdraw():
    # Step 3: Test withdrawal
    result = withdraw(100, 30)
    assert result == 70
