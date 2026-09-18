# test_did_not_raise.py
# What happens when pytest.raises does not get what it expects?
# Run it with:  pytest -v test_did_not_raise.py
# BOTH tests FAIL on purpose.

# Step 1 - Import pytest and the function we are testing
import pytest
from user_registration import create_user


# Step 2 - Valid input raises no exception at all
def test_no_exception_raised():
    with pytest.raises(ValueError):
        create_user("alice", 20, "alice@example.com")


# Step 3 - An exception is raised, but its message does not match
def test_wrong_message():
    with pytest.raises(ValueError, match="Age is too low"):
        create_user("alice", 10, "alice@example.com")
