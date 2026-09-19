# test_payment.py
# Run it with:  pytest -v -s test_payment.py

from unittest.mock import Mock, patch

from payment import get_price


def test_price():

    # Step 1: Create a fake response object
    fake_response = Mock()

    # Step 2: Decide what the fake object returns from .json()
    fake_response.json.return_value = {"price": 100}

    # Step 3: Replace requests.get with a Mock, but ONLY inside this
    #         with block. patch() puts the real requests.get back
    #         automatically when the block ends.
    with patch("payment.requests.get", return_value=fake_response) as fake_get:

        # Step 4: Run the application code
        result = get_price("book")
        print(f"\n[TEST] get_price returned {result}")

        # Step 5: Check which URL the code asked for
        fake_get.assert_called_once_with("https://example.com/products/book")

    # Step 6: Check the result
    assert result == 100
