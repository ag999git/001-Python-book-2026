# test_q01_aaa.py - Question 1: Arrange, Act, Assert
# Run it with:  pytest -v test_q01_aaa.py

from calculator import square


def test_square_of_ten():
    # Step 1 - Arrange: prepare the input
    number = 10

    # Step 2 - Act: call the code being tested
    result = square(number)

    # Step 3 - Assert: check the result
    assert result == 100


def test_square_of_negative_number():
    # An edge case: the square of a negative number is positive
    assert square(-3) == 9
