# test_q15_parametrize.py - Questions 14 and 15: one test, many inputs
# Run it with:  pytest -v test_q15_parametrize.py

import pytest
from calculator import add


# Step 1 - Each tuple is (input, expected): here, add(input, 1) should give expected
@pytest.mark.parametrize(
    "input,expected",
    [
        (1, 2),
        (3, 4),
        (5, 6),
    ],
)
# Step 2 - pytest runs this function once for each tuple
def test_add(input, expected):
    assert add(input, 1) == expected
