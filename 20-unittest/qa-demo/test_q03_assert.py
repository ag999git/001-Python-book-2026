# test_q03_assert.py - Question 3: what pytest shows when an assert fails
# Run it with:  pytest test_q03_assert.py
# This test FAILS on purpose.

from calculator import add_buggy


def test_add_two_and_two():
    # 2 + 2 should be 4, but add_buggy has a deliberate bug
    assert add_buggy(2, 2) == 4
