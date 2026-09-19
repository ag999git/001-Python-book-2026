# mock_vs_magicmock.py
# What happens when a plain Mock and a MagicMock meet special operations?

# Step 1 - Import both classes
from unittest.mock import Mock, MagicMock

plain = Mock()
magic = MagicMock()

# Step 2 - A list of operations to try, each written as a small function
operations = [
    ("len(obj)", lambda obj: len(obj)),
    ("list(obj)", lambda obj: list(obj)),
    ('"a" in obj', lambda obj: "a" in obj),
    ("bool(obj)", lambda obj: bool(obj)),
]

# Step 3 - Try each operation on both objects
for label, operation in operations:
    for name, obj in [("Mock", plain), ("MagicMock", magic)]:
        try:
            print(f"{name:9} {label:11} -> {operation(obj)!r}")
        except TypeError as error:
            print(f"{name:9} {label:11} -> TypeError: {error}")

# Step 4 - A plain Mock can support len() only if we add __len__ ourselves
plain.__len__ = Mock(return_value=5)
print("Mock after adding __len__ by hand -> len =", len(plain))
