# bank_account.py
# Core application logic: a simple bank account.


class BankAccount:

    # Step 1 - Create an account with an owner and an opening balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Step 2 - Add money to the account
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    # Step 3 - Take money out of the account
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    # Step 4 - Report the current balance
    def get_balance(self):
        return self.balance
