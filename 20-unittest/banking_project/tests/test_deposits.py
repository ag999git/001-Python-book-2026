# File: tests/test_deposits.py
# Notice: there is NO import statement for conftest.py or fresh_account.
# Pytest finds fresh_account in tests/conftest.py by itself.


def test_deposit(fresh_account):
    # Step 1 - Show which file is running and the starting balance
    print("[TEST] Running deposit inside test_deposits.py")
    print(f"[TEST] Starting balance: {fresh_account.get_balance()}")

    # Step 2 - Deposit 50 and check the new balance
    fresh_account.deposit(50)
    print(f"[TEST] Balance after deposit: {fresh_account.get_balance()}")
    assert fresh_account.get_balance() == 150
