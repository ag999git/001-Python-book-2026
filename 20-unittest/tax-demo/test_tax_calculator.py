# test_tax_calculator.py
# First attempt: one separate test function for every price (repetitive).
# Run it with:  pytest -v test_tax_calculator.py

# Step 1 - Import the function we want to test
from tax_calculator import calculate_tax


# Step 2 - Test case 1: a price of 1.00 should give a tax of 0.10 (10% of 1.00)
def test_tax_1():
    assert calculate_tax(1.00) == 0.10


# Step 3 - Test case 2: a price of 1.10 should give a tax of 0.11 (10% of 1.10)
def test_tax_2():
    assert calculate_tax(1.10) == 0.11


# Step 4 - Test case 3: a price of 2.00 should give a tax of 0.20 (10% of 2.00)
def test_tax_3():
    assert calculate_tax(2.00) == 0.20
