# test_calculator.py
# Run it with:  pytest -v test_calculator.py

# Step 1: Import the application function
from calculator import multiply


def test_multiply():

    # Step 2: Call the function
    result = multiply(5, 4)

    # Step 3: Check the returned value
    assert result == 20

    # Step 4: Check the type as well
    assert isinstance(result, int)
