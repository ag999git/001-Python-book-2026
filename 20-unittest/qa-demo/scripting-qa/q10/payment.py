# payment.py
# Needs the requests library:  python -m pip install requests

import requests


def get_price(product):

    # Step 1: A real program would contact an internet API
    response = requests.get(f"https://example.com/products/{product}")

    # Step 2: Read the price from the JSON reply
    return response.json()["price"]
