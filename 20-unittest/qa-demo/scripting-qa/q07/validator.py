# validator.py


def check_age(age):

    # Step 1: Validate the age
    if age < 18:
        # Step 2: Return the "invalid" message
        return "not allowed"

    # Step 3: Return the "valid" message
    return "allowed"
