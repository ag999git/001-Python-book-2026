# test_calculator.py
# Run it with:  pytest -v -s test_calculator.py

import pytest

from calculator import divide, calculate_tax


# Part A - Testing exceptions
def test_exception():

    # Step 1: Tell pytest that an exception is expected
    with pytest.raises(ValueError, match="cannot divide"):

        # Step 2: Code that should raise the exception
        divide(10, 0)


# Part B - Testing floating-point values
def test_tax():

    result = calculate_tax(1.10)
    print(f"\n[TEST] calculate_tax(1.10) = {result!r}")

    # Step 1: Do not compare floats exactly.
    #         result == 0.11 would be False here.
    assert result == pytest.approx(0.11)
