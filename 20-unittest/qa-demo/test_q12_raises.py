# test_q12_raises.py - Questions 12 and 13: testing exceptions and messages
# Run it with:  pytest -v test_q12_raises.py

import pytest
from calculator import set_age


# Step 1 - Check only the exception type
def test_int_of_text_raises():
    with pytest.raises(ValueError):
        int("abc")


# Step 2 - Check the type AND part of the message
def test_negative_age_message():
    with pytest.raises(ValueError, match="invalid age"):
        set_age(-5)
