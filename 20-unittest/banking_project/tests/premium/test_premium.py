# File: tests/premium/test_premium.py
# This test uses TWO fixtures from TWO different conftest.py files:
#   premium_account -> from tests/premium/conftest.py (same folder)
#   fresh_account   -> from tests/conftest.py (the parent folder)


def test_transfer_to_regular(premium_account, fresh_account):
    # Step 1 - Show both starting balances
    print(f"[TEST] Premium starts with {premium_account.get_balance()}, "
          f"regular starts with {fresh_account.get_balance()}")

    # Step 2 - Move 500 from the premium account to the regular account
    premium_account.withdraw(500)
    fresh_account.deposit(500)
    print(f"[TEST] Premium now {premium_account.get_balance()}, "
          f"regular now {fresh_account.get_balance()}")

    # Step 3 - Check both balances
    assert premium_account.get_balance() == 9500
    assert fresh_account.get_balance() == 600
