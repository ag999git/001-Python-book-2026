# test_validator.py
# Run it with:  pytest -v test_validator.py

import pytest

from validator import check_age


# Step 1: Create several test cases: two invalid and two valid ages.
#         17 and 18 are the boundary values, where mistakes often hide.
@pytest.mark.parametrize(
    "age, expected",
    [
        (10, "not allowed"),
        (17, "not allowed"),
        (18, "allowed"),
        (25, "allowed"),
    ],
)
def test_age_check(age, expected):

    # Step 2: Run the function
    result = check_age(age)

    # Step 3: Check the output
    assert result == expected
