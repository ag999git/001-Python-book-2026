# di_without_pytest.py
# Dependency injection in plain Python, without pytest.
# Run it with:  python di_without_pytest.py


# Step 1 - Two classes that can play the role of "a database"
class RealDatabase:
    def get_user_count(self):
        print("   [RealDatabase] Pretending to query a slow, real database...")
        return 1520


class FakeDatabase:
    """A simple stand-in used for testing. It always returns a fixed value."""
    def get_user_count(self):
        print("   [FakeDatabase] Returning a fixed test value instantly")
        return 3


# Step 2 - WITHOUT dependency injection:
# the function creates its own database inside itself,
# so it is tied (coupled) to RealDatabase and cannot use anything else.
def report_without_di():
    database = RealDatabase()
    return f"Total users: {database.get_user_count()}"


# Step 3 - WITH dependency injection:
# the function receives the database as a parameter.
# It does not know or care which kind of database it gets.
def report_with_di(database):
    return f"Total users: {database.get_user_count()}"


# Step 4 - Use the functions
print("1. Without dependency injection:")
print("  ", report_without_di())

print("2. With dependency injection, given a real database:")
print("  ", report_with_di(RealDatabase()))

print("3. With dependency injection, given a fake database (for a test):")
result = report_with_di(FakeDatabase())
print("  ", result)

# Step 5 - A simple check, like a test would do
assert result == "Total users: 3"
print("4. Check passed: the report works correctly with the fake database")
