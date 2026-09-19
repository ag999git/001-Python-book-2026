# test_three_approaches.py
# Runs the three styles of exception test against the CORRECT and the
# BROKEN version of create_user(). A good test must PASS for the correct
# version and FAIL for the broken one.
# Run it with:  pytest -v test_three_approaches.py

# Step 1 - Import pytest and both versions of the function
import pytest
import user_service
import user_service_broken


# Step 2 - Approach A: try/except without else (the incorrect approach)
def check_try_except_only(create_user):
    try:
        create_user(10)
    except ValueError:
        pass


# Step 3 - Approach B: try/except/else (the improved manual approach)
def check_try_except_else(create_user):
    try:
        create_user(10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError was not raised"


# Step 4 - Approach C: pytest.raises (the recommended approach)
def check_pytest_raises(create_user):
    with pytest.raises(ValueError):
        create_user(10)


# Step 5 - Run each approach against each version
def test_A_try_except_only_correct():
    check_try_except_only(user_service.create_user)

def test_A_try_except_only_broken():
    check_try_except_only(user_service_broken.create_user)

def test_B_try_except_else_correct():
    check_try_except_else(user_service.create_user)

def test_B_try_except_else_broken():
    check_try_except_else(user_service_broken.create_user)

def test_C_pytest_raises_correct():
    check_pytest_raises(user_service.create_user)

def test_C_pytest_raises_broken():
    check_pytest_raises(user_service_broken.create_user)
