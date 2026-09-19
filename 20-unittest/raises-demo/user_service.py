# user_service.py
# The CORRECT version of create_user().

def create_user(age):
    # Step 1 - Business rule: users must be at least 13 years old
    if age < 13:
        raise ValueError("User must be at least 13 years old")
    # Step 2 - The age is acceptable
    return "User created"
