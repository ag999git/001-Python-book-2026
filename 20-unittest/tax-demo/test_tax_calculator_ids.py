# test_tax_calculator_ids.py
# Giving each parameter set a readable name with 'ids'.
# To run the tests in this file, use the command: pytest -v test_tax_calculator_ids.py

# Step 1 - Import pytest and the function under test
import pytest
from tax_calculator import calculate_tax


# Step 2 - One name in 'ids' for each tuple, in the same order
@pytest.mark.parametrize(
    "price, expected",
    [
        (1.00, 0.10),
        (1.10, 0.11),
        (0.00, 0.00),
        (999.99, 99.999),
    ],
    ids=["basic price", "price with decimals", "free item", "large price"],
)
# Step 3 - The test itself is unchanged
def test_tax_values(price, expected):
    assert calculate_tax(price) == pytest.approx(expected)
