# test_square.py
# Run it with:  pytest -v -s test_square.py

# Step 1: Import pytest (not strictly needed for a plain assert,
#         but most test files import it, so it is a good habit)
import pytest

# Step 2: Import the function to be tested
from square import square


# Step 3: Create a test function (its name must start with test)
def test_square():

    # Step 4 (Arrange): Prepare the input
    number = 5

    # Step 5 (Act): Call the application function
    result = square(number)
    print(f"\n[TEST] square({number}) returned {result}")

    # Step 6 (Assert): Check the returned value
    assert result == 25
