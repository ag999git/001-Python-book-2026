# test_user_registration.py
# To run the tests in this file, use the command:
#     pytest -v test_user_registration.py
# Add -s to see the print() messages:
#     pytest -v -s test_user_registration.py

# Step 1 - Import pytest and the function we are testing
import pytest
# user_registration.py contains the create_user function that we are testing.
from user_registration import create_user


# Step 2 - Test that an exception is raised (type only)
def test_empty_username():
    # Test that ValueError is raised when the username is empty.
    # The test passes only if the code inside the 'with' block raises ValueError.
    with pytest.raises(ValueError):
        create_user("", 20, "alice@example.com")


# Step 3 - Test the exception type AND its message
def test_username_message():
    # 'match' checks that the exception message contains
    # the text "Username cannot be empty"
    with pytest.raises(ValueError, match="Username cannot be empty"):
        create_user("", 20, "alice@example.com")


# Step 4 - Capture the exception with 'as excinfo' and inspect it
def test_underage_user():
    with pytest.raises(ValueError) as excinfo:
        create_user("alice", 10, "alice@example.com")

    # The checks below run AFTER the 'with' block, outside it
    print(f"\n   Captured type: {excinfo.type.__name__}")
    print(f"   Captured message: {excinfo.value}")

    assert excinfo.type is ValueError             # The exception type is ValueError
    assert "13 years old" in str(excinfo.value)   # The message mentions "13 years old"


# Step 5 - Test the email check
def test_invalid_email():
    with pytest.raises(ValueError, match="Invalid email address"):
        create_user("alice", 20, "bad-email")


# Step 6 - Test the "happy path": valid input gives a correct user record
def test_valid_user():
    user = create_user("alice", 20, "alice@example.com")
    print(f"\n   Returned user: {user}")

    assert user["username"] == "alice"            # The username is correct
    assert user["age"] == 20                      # The age is correct
    assert user["email"] == "alice@example.com"   # The email is correct


# Step 7 - The older "functional form" of pytest.raises
def test_functional_form():
    # The function and its arguments are passed to pytest.raises separately.
    # pytest.raises calls create_user("", 20, "alice@example.com") itself.
    excinfo = pytest.raises(ValueError, create_user, "", 20, "alice@example.com")
    print(f"\n   Functional form captured: {excinfo.value}")
    assert "Username cannot be empty" in str(excinfo.value)
