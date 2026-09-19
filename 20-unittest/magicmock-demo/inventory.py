# inventory.py
# Small functions that use special Python operations.
# They are the "code under test" for test_inventory.py.


# Step 1 - Uses len()
def count_items(container):
    return len(container)


# Step 2 - Uses a for loop (iteration)
def total_quantity(stock):
    total = 0
    for quantity in stock:
        total += quantity
    return total


# Step 3 - Uses the 'in' operator
def is_available(item, warehouse):
    return item in warehouse


# Step 4 - Uses dictionary-style access
def get_database_url(config):
    return f"{config['host']}:{config['port']}"


# Step 5 - Uses a with block and open()
def read_greeting(path):
    with open(path) as f:
        return f.read().strip()
