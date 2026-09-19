# ex4_iter_pitfall.py - Why return_value should be a list, not iter([...])

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Give __iter__ a ready-made iterator instead of a list
data = MagicMock()
data.__iter__.return_value = iter([10, 20, 30])

# Step 3 - The first loop uses up the iterator
print("First loop:", list(data))

# Step 4 - The same, used-up iterator is returned again, so nothing is left
print("Second loop:", list(data))
