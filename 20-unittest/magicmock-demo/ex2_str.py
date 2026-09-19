# ex2_str.py - Simulating string conversion

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be a user object
user = MagicMock()

# Step 3 - Tell its __str__ method what to return
user.__str__.return_value = "John"

# Step 4 - print() converts the object to text by calling str(user),
#          which in turn calls user.__str__()
print(user)
print("Using str() directly:", str(user))
