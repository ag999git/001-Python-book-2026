# bank_account.py
# The application code: a simple bank account.


class BankAccount:

    # Step 1 - Create the account with an owner and an opening balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Step 2 - Add money
    def deposit(self, amount):
        self.balance += amount

    # Step 3 - Take money out, refusing if there is not enough
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    # Step 4 - Report the balance (the tests use this method)
    def get_balance(self):
        return self.balance
