# File: tests/test_withdrawals.py
# Notice: fresh_account is injected by pytest from tests/conftest.py.
# Again, no import statement is needed.


def test_withdraw(fresh_account):
    # Step 1 - Show which file is running and the starting balance
    print("[TEST] Running withdraw inside test_withdrawals.py")
    print(f"[TEST] Starting balance: {fresh_account.get_balance()}")

    # Step 2 - Withdraw 30 and check the new balance
    fresh_account.withdraw(30)
    print(f"[TEST] Balance after withdrawal: {fresh_account.get_balance()}")
    assert fresh_account.get_balance() == 70
