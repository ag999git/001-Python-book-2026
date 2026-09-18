# user_registration.py
# This module contains the create_user function that we want to test.

# Step 1 - Import the regular expression module, used to check email addresses
import re


def create_user(username, age, email):
    """
    Create a user record (a dictionary) after checking the input.

    Raises ValueError as soon as one of the checks fails:
      - the username is empty
      - the age is less than 13
      - the email address does not look valid
    """

    # Step 2 - Check the username.
    # 'not username' is True for an empty string "" and for None.
    if not username:
        raise ValueError("Username cannot be empty")

    # Step 3 - Check the age (a business rule: users must be 13 or older)
    if age < 13:
        raise ValueError("User must be at least 13 years old")

    # Step 4 - Check that the email roughly looks like name@domain.ext
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        raise ValueError("Invalid email address")

    # Step 5 - All checks passed, so build and return the user record
    return {
        "username": username,
        "age": age,
        "email": email,
    }

