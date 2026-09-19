# ex3_contains.py - Simulating membership testing

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be a container
container = MagicMock()

# Step 3 - Make __contains__ always answer True
container.__contains__.return_value = True

# Step 4 - The 'in' operator calls container.__contains__("apple")
print('"apple" in container ->', "apple" in container)

# Step 5 - Note: with return_value, EVERY item is "found"
print('"brick" in container ->', "brick" in container)

# Step 6 - To answer differently for different items, use side_effect
#          with a function that decides for each item
container.__contains__.side_effect = lambda item: item in ["apple", "banana"]
print('After side_effect, "apple" in container ->', "apple" in container)
print('After side_effect, "brick" in container ->', "brick" in container)
