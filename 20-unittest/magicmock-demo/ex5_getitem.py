# ex5_getitem.py - Simulating dictionary access

# Step 1 - Import MagicMock
from unittest.mock import MagicMock

# Step 2 - Create a MagicMock that will pretend to be a settings dictionary
config = MagicMock()

# Step 3 - config[...] calls config.__getitem__(key); give it a return value
config.__getitem__.return_value = "localhost"
print('config["host"] =', config["host"])

# Step 4 - return_value gives the SAME answer for every key
print('config["port"] =', config["port"])

# Step 5 - For a different answer per key, use side_effect with a real dict.
#          The dict's own __getitem__ is used, so a missing key raises KeyError.
settings = {"host": "localhost", "port": 5432}
config.__getitem__.side_effect = settings.__getitem__
print('After side_effect, config["host"] =', config["host"])
print('After side_effect, config["port"] =', config["port"])

# Step 6 - Check which key was asked for last
print("Last key asked for:", config.__getitem__.call_args)
