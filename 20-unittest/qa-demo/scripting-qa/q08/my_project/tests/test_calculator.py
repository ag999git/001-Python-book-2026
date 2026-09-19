# tests/test_calculator.py
# Test file

from calculator import add


def test_add():

    # Step 1: Call the application function
    result = add(2, 3)

    # Step 2: Check the result
    assert result == 5
