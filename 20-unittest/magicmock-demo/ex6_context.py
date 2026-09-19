# ex6_context.py - Simulating a context manager

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be an open file
fake_file = MagicMock()

# Step 3 - 'with fake_file as f' puts the result of __enter__() into f.
#          By default __enter__ returns a DIFFERENT, new MagicMock,
#          so we tell it to return fake_file itself.
fake_file.__enter__.return_value = fake_file

# Step 4 - Tell the read() method what text to return
fake_file.read.return_value = "Hello"

# Step 5 - Use the fake file exactly as a real one would be used
with fake_file as f:
    print(f.read())

# Step 6 - Check that the with block really entered and exited
print("__enter__ called:", fake_file.__enter__.called)
print("__exit__ called:", fake_file.__exit__.called)
print("__exit__ was called with:", fake_file.__exit__.call_args)
