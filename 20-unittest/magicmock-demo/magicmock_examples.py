# magicmock_examples.py
# All six MagicMock examples in one script.
# Run it with:  python magicmock_examples.py

from unittest.mock import MagicMock

# ------------------------------------------------------------
# Example 1: Simulating len()
# ------------------------------------------------------------
print("\n=== Example 1: Simulating len() ===")

# Step 1 - Create a MagicMock that will pretend to be a list
fake_list = MagicMock()

# Step 2 - Tell its __len__ method what to return
fake_list.__len__.return_value = 5

# Step 3 - len() calls fake_list.__len__() behind the scenes
print("len(fake_list) =", len(fake_list))

# Step 4 - A mock also records how it was used
print("Was __len__ called?", fake_list.__len__.called)


# ------------------------------------------------------------
# Example 2: Simulating string conversion
# ------------------------------------------------------------
print("\n=== Example 2: Simulating string conversion ===")

# Step 1 - Create a MagicMock that will pretend to be a user object
user = MagicMock()

# Step 2 - Tell its __str__ method what to return
user.__str__.return_value = "John"

# Step 3 - print() converts the object to text by calling str(user),
#          which in turn calls user.__str__()
print(user)
print("Using str() directly:", str(user))


# ------------------------------------------------------------
# Example 3: Simulating membership testing
# ------------------------------------------------------------
print("\n=== Example 3: Simulating membership testing ===")

# Step 1 - Create a MagicMock that will pretend to be a container
container = MagicMock()

# Step 2 - Make __contains__ always answer True
container.__contains__.return_value = True

# Step 3 - The 'in' operator calls container.__contains__("apple")
print('"apple" in container ->', "apple" in container)

# Step 4 - Note: with return_value, EVERY item is "found"
print('"brick" in container ->', "brick" in container)

# Step 5 - To answer differently for different items, use side_effect
#          with a function that decides for each item
container.__contains__.side_effect = lambda item: item in ["apple", "banana"]
print('After side_effect, "apple" in container ->', "apple" in container)
print('After side_effect, "brick" in container ->', "brick" in container)


# ------------------------------------------------------------
# Example 4: Simulating iteration
# ------------------------------------------------------------
print("\n=== Example 4: Simulating iteration ===")

# Step 1 - Create a MagicMock that will pretend to be a collection
data = MagicMock()

# Step 2 - Give __iter__ a LIST of values.
#          MagicMock turns the list into a fresh iterator every time
#          the object is looped over, so it can be looped over many times.
data.__iter__.return_value = [10, 20, 30]

# Step 3 - The for loop calls iter(data), which calls data.__iter__()
print("First loop:")
for item in data:
    print(item)

# Step 4 - Loop again: the values are still there
print("Second loop:", list(data))


# ------------------------------------------------------------
# Example 5: Simulating dictionary access
# ------------------------------------------------------------
print("\n=== Example 5: Simulating dictionary access ===")

# Step 1 - Create a MagicMock that will pretend to be a settings dictionary
config = MagicMock()

# Step 2 - config[...] calls config.__getitem__(key); give it a return value
config.__getitem__.return_value = "localhost"
print('config["host"] =', config["host"])

# Step 3 - return_value gives the SAME answer for every key
print('config["port"] =', config["port"])

# Step 4 - For a different answer per key, use side_effect with a real dict.
#          The dict's own __getitem__ is used, so a missing key raises KeyError.
settings = {"host": "localhost", "port": 5432}
config.__getitem__.side_effect = settings.__getitem__
print('After side_effect, config["host"] =', config["host"])
print('After side_effect, config["port"] =', config["port"])

# Step 5 - Check which key was asked for last
print("Last key asked for:", config.__getitem__.call_args)


# ------------------------------------------------------------
# Example 6: Simulating a context manager
# ------------------------------------------------------------
print("\n=== Example 6: Simulating a context manager ===")

# Step 1 - Create a MagicMock that will pretend to be an open file
fake_file = MagicMock()

# Step 2 - 'with fake_file as f' puts the result of __enter__() into f.
#          By default __enter__ returns a DIFFERENT, new MagicMock,
#          so we tell it to return fake_file itself.
fake_file.__enter__.return_value = fake_file

# Step 3 - Tell the read() method what text to return
fake_file.read.return_value = "Hello"

# Step 4 - Use the fake file exactly as a real one would be used
with fake_file as f:
    print(f.read())

# Step 5 - Check that the with block really entered and exited
print("__enter__ called:", fake_file.__enter__.called)
print("__exit__ called:", fake_file.__exit__.called)
print("__exit__ was called with:", fake_file.__exit__.call_args)
