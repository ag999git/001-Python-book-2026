# bank_account.py
"""
A small BankAccount class used by the test examples.
It is kept simple on purpose so that we can focus on the tests.
"""


class BankAccount:
    # Step 1 - Create the account with an owner, a balance and a status
    def __init__(self, owner, balance=0, status="active"):
        self.owner = owner
        self.balance = balance
        self.status = status          # "active" or "frozen"

    # Step 2 - Add money to the account
    def deposit(self, amount):
        if self.status == "frozen":
            raise ValueError("Account is frozen")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    # Step 3 - Take money out of the account
    def withdraw(self, amount):
        if self.status == "frozen":
            raise ValueError("Account is frozen")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    # Step 4 - Report the current balance
    def get_balance(self):
        return self.balance


# Step 5 - A simple helper that does not need an account at all
def format_currency(amount):
    """Return an amount as text, for example 1500 -> 'Rs. 1,500.00'."""
    return f"Rs. {amount:,.2f}"

