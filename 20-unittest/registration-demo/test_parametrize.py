# test_parametrize.py
# One test function, run once for each row of invalid input.
# Run it with:  pytest -v test_parametrize.py

# Step 1 - Import pytest and the function we are testing
import pytest
from user_registration import create_user


# Step 2 - Each tuple is one test case:
#          (username, age, email, text expected in the error message)
@pytest.mark.parametrize(
    "username, age, email, expected_message",
    [
        ("", 20, "alice@example.com", "Username cannot be empty"),
        (None, 20, "alice@example.com", "Username cannot be empty"),
        ("alice", 12, "alice@example.com", "at least 13 years old"),
        ("alice", 20, "alice.example.com", "Invalid email address"),
        ("alice", 20, "alice@example", "Invalid email address"),
        ("alice", 20, "alice@@example.com", "Invalid email address"),
    ],
)
# Step 3 - pytest runs this function once for every tuple above
def test_invalid_input(username, age, email, expected_message):
    with pytest.raises(ValueError, match=expected_message):
        create_user(username, age, email)
