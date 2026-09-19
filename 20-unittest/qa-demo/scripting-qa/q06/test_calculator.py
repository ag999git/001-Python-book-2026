# test_calculator.py
# Run it with:  pytest -v test_calculator.py

import pytest

from calculator import square


# Step 1: parametrize runs the same test several times,
#         each time with a different set of values.
@pytest.mark.parametrize(
    "number, expected",
    [
        (2, 4),
        (3, 9),
        (5, 25),
        (10, 100),
    ],
)
def test_square(number, expected):

    # Step 2: Each row of data becomes one test run
    result = square(number)

    # Step 3: Compare the actual result with the expected result
    assert result == expected
