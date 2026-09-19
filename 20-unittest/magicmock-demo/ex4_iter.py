# ex4_iter.py - Simulating iteration

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be a collection
data = MagicMock()

# Step 3 - Give __iter__ a LIST of values.
#          MagicMock turns the list into a fresh iterator every time
#          the object is looped over, so it can be looped over many times.
data.__iter__.return_value = [10, 20, 30]

# Step 4 - The for loop calls iter(data), which calls data.__iter__()
print("First loop:")
for item in data:
    print(item)

# Step 5 - Loop again: the values are still there
print("Second loop:", list(data))
