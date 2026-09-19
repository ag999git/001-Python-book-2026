# tests/test_product.py
# Run it from the student_project folder with:  pytest -v -s

import pytest

from product import Product


@pytest.fixture
def product():
    # Step 1: Create the common object
    print("\n[FIXTURE] creating product")
    return Product("Book", 100)


def test_product_name(product):
    # Step 2: Test the name
    assert product.name == "Book"


def test_product_price(product):
    # Step 3: Test the method result
    result = product.get_price()
    assert result == 100


@pytest.mark.parametrize("value", [100, 200, 300])
def test_multiple_prices(value):
    # Step 4: Test several values
    p = Product("Item", value)
    assert p.get_price() == value
