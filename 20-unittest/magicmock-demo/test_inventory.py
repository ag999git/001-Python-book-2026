# test_inventory.py
# Tests for inventory.py that use MagicMock instead of real
# lists, dictionaries and files.
# Run it with:  pytest -v -s test_inventory.py

# Step 1 - Imports
from unittest.mock import MagicMock, mock_open, patch
from inventory import (count_items, total_quantity, is_available,
                       get_database_url, read_greeting)


# Step 2 - Test len() with __len__
def test_count_items():
    container = MagicMock()
    container.__len__.return_value = 3
    result = count_items(container)
    print(f"\n   count_items returned {result}")
    assert result == 3
    container.__len__.assert_called_once()   # len() was used exactly once


# Step 3 - Test a for loop with __iter__
def test_total_quantity():
    stock = MagicMock()
    stock.__iter__.return_value = [5, 10, 15]
    result = total_quantity(stock)
    print(f"\n   total_quantity returned {result}")
    assert result == 30


# Step 4 - Test 'in' with __contains__, and check what was asked for
def test_is_available():
    warehouse = MagicMock()
    warehouse.__contains__.return_value = True
    assert is_available("pen", warehouse) is True
    warehouse.__contains__.assert_called_once_with("pen")
    print("\n   __contains__ was called with 'pen'")


# Step 5 - Test dictionary access with a different value for each key
def test_get_database_url():
    config = MagicMock()
    config.__getitem__.side_effect = {"host": "db.example.com", "port": 5432}.__getitem__
    result = get_database_url(config)
    print(f"\n   get_database_url returned {result}")
    assert result == "db.example.com:5432"


# Step 6 - Test a function that opens a file, without any real file.
#          patch() swaps the built-in open() for a fake one during the with block.
#          mock_open() builds that fake: a MagicMock set up to act like a file.
def test_read_greeting():
    fake_open = mock_open(read_data="Hello from a fake file\n")
    with patch("builtins.open", fake_open):
        result = read_greeting("greeting.txt")
    print(f"\n   read_greeting returned {result!r}")
    assert result == "Hello from a fake file"
    fake_open.assert_called_once_with("greeting.txt")   # the right file name was used
