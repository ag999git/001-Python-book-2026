# user_service_broken.py
# A BROKEN version of create_user(), used only to test our tests.
# Someone mistyped 13 as 1, so an age of 10 no longer raises an error.

def create_user(age):
    # Step 1 - The bug: the check should be 'age < 13'
    if age < 1:
        raise ValueError("User must be at least 13 years old")
    # Step 2 - An age of 10 now reaches this line
    return "User created"
