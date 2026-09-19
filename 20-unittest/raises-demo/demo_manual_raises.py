# demo_manual_raises.py
# A simplified, home-made version of what pytest.raises does,
# so that we can watch each step. Run it with: python demo_manual_raises.py

# Step 1 - Import the correct and broken versions of the function
import user_service
import user_service_broken


# Step 2 - A simple checker that works like pytest.raises
def expect_error(func, value, expected_error):
    try:
        func(value)
    except expected_error as error:
        # The expected error happened: the check passes
        print(f"   PASS: {expected_error.__name__} raised -> {error}")
    else:
        # No error happened: the check must fail
        print(f"   FAIL: DID NOT RAISE {expected_error.__name__}")


# Step 3 - Try it on both versions
print("Correct version, age 10:")
expect_error(user_service.create_user, 10, ValueError)

print("Broken version, age 10:")
expect_error(user_service_broken.create_user, 10, ValueError)
