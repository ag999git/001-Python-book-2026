# tests/test_more_math.py
# A second test file, to show that pytest finds every test_*.py file

from calculator import add


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def helper_not_a_test():
    # Not collected: the name does not start with "test"
    return 42
