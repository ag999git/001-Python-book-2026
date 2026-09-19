# calculator.py


def divide(a, b):

    # Step 1: Check for an invalid operation
    if b == 0:
        # Step 2: Raise an exception with a clear message
        raise ValueError("division by zero")

    # Step 3: Normal calculation
    return a / b
