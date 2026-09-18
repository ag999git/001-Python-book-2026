# test_bank_xunit.py
# Classic xUnit style: all tests live inside one class
# and share one setup_method and one teardown_method.

from bank_account import BankAccount, format_currency


class TestBankAccount:

    # Step 1 - Setup: runs before EVERY test method in this class
    def setup_method(self, method):
        print(f"\n[setup] Creating account for {method.__name__}")
        self.account = BankAccount("John", 100)

    # Step 2 - Teardown: runs after EVERY test method in this class
    def teardown_method(self, method):
        print(f"\n[teardown] Finished {method.__name__}")

    # Step 3 - A test that really needs the account
    def test_deposit(self):
        self.account.deposit(50)
        print("Balance after deposit:", self.account.get_balance())
        assert self.account.get_balance() == 150

    # Step 4 - Another test that needs the account
    def test_withdraw(self):
        self.account.withdraw(30)
        print("Balance after withdrawal:", self.account.get_balance())
        assert self.account.get_balance() == 70

    # Step 5 - A test that does NOT need the account,
    #          but setup_method still creates one for it
    def test_format_currency(self):
        result = format_currency(1500)
        print("Formatted amount:", result)
        assert result == "Rs. 1,500.00"
