# demo_registration.py
# Try create_user() with good and bad input and see what happens.
# Run it with:  python demo_registration.py

# Step 1 - Import the function we want to try
from user_registration import create_user

# Step 2 - A list of test cases: (username, age, email)
test_cases = [
    ("alice", 20, "alice@example.com"),   # valid
    ("", 20, "alice@example.com"),        # empty username
    (None, 20, "alice@example.com"),      # missing username
    ("alice", 10, "alice@example.com"),   # too young
    ("alice", 20, "bad-email"),           # invalid email
    ("", 10, "bad-email"),                # three problems at once
]

# Step 3 - Try each case. try/except catches the ValueError so that
#          the program can print the message and carry on with the next case.
for number, (username, age, email) in enumerate(test_cases, start=1):
    print(f"{number}. create_user({username!r}, {age}, {email!r})")
    try:
        user = create_user(username, age, email)
        print(f"   Success: {user}")
    except ValueError as error:
        print(f"   ValueError: {error}")
