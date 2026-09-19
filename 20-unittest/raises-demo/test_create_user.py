# test_create_user.py
# A complete set of black-box tests for create_user().
# Each test checks one observable behaviour.
# Run it with:  pytest -v test_create_user.py

# Step 1 - Import pytest and the function under test
import pytest
from user_service import create_user


# Step 2 - An invalid age must raise ValueError with the right message
def test_age_10_is_rejected():
    with pytest.raises(ValueError, match="at least 13"):
        create_user(10)


# Step 3 - A valid age must succeed
def test_age_14_is_accepted():
    assert create_user(14) == "User created"


# Step 4 - The boundary: 12 is the last age refused, 13 the first accepted
def test_age_12_is_rejected():
    with pytest.raises(ValueError):
        create_user(12)


def test_age_13_is_accepted():
    assert create_user(13) == "User created"
