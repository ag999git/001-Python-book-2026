# test_tax_calculator2.py
# This file contains tests for the calculate_tax function in tax_calculator.py.
# To run the tests in this file, use the command: pytest -v test_tax_calculator2.py

# Step 1 - Import pytest and the function under test
import pytest
from tax_calculator import calculate_tax


# Step 2 - Use @pytest.mark.parametrize to run the same test with several sets of data.
#   "price, expected" names the two arguments the test function receives.
#   The list of tuples holds the data sets: (input, expected result).
@pytest.mark.parametrize("price, expected", [
    (1.00, 0.10),
    (1.10, 0.11),
    (2.00, 0.20),
    (5.50, 0.55),
    (10.00, 1.00),
])
# Step 3 - One test function, run once for each tuple above
def test_tax_values(price, expected):
    assert calculate_tax(price) == expected
