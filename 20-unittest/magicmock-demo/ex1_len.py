# ex1_len.py - Simulating len()

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be a list
fake_list = MagicMock()

# Step 3 - Tell its __len__ method what to return
fake_list.__len__.return_value = 5

# Step 4 - len() calls fake_list.__len__() behind the scenes
print("len(fake_list) =", len(fake_list))

# Step 5 - A mock also records how it was used
print("Was __len__ called?", fake_list.__len__.called)
