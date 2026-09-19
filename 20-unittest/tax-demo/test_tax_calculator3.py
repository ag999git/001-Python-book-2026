# test_tax_calculator3.py
# This file contains tests for the calculate_tax function in tax_calculator.py.
# To run the tests in this file, use the command: pytest -v test_tax_calculator3.py

# Step 1 - Import pytest and the function under test
import pytest
from tax_calculator import calculate_tax


# Step 2 - The same five data sets as before
@pytest.mark.parametrize("price, expected", [
    (1.00, 0.10),
    (1.10, 0.11),
    (2.00, 0.20),
    (5.50, 0.55),
    (10.00, 1.00),
])
# Step 3 - Compare with pytest.approx instead of plain ==
def test_tax_values(price, expected):
    # pytest.approx allows a very small difference (tolerance),
    # so tiny floating-point errors do not make the test fail.
    assert calculate_tax(price) == pytest.approx(expected)
