# calculator.py


def divide(a, b):

    # Step 1: Check for an invalid division
    if b == 0:
        raise ValueError("cannot divide by zero")

    # Step 2: Normal calculation
    return a / b


def calculate_tax(amount):
    # 10% tax
    return amount * 0.10
