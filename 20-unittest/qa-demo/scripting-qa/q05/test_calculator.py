# test_calculator.py
# Run it with:  pytest -v test_calculator.py

import pytest

from calculator import divide


def test_divide_exception():

    # Step 1: Tell pytest that an exception is expected
    with pytest.raises(ValueError, match="division by zero"):

        # Step 2: The code inside this block should raise the exception
        divide(10, 0)


def test_divide_normal():
    # Step 3: Also check that normal division still works
    assert divide(10, 2) == 5
