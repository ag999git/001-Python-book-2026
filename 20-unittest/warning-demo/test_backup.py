# test_backup.py
# A test that uses a custom marker which has not been registered yet.

# Step 1 - Import pytest so that we can use pytest.mark
import pytest


# Step 2 - Label the test with our own marker, 'slow'
@pytest.mark.slow  # A custom marker we invented
def test_database_backup():
    pass
