# conftest.py
"""
Fixtures placed in a file named conftest.py are shared automatically with
every test file in this folder (and in the folders inside it).
The test files do not need to import them.
"""

# Step 1 - Import pytest and the class we want to test
import pytest
from payment_gateway import PaymentGateway


# Step 2 - One session-scoped gateway for all the test files
@pytest.fixture(scope="session")
def shared_gateway():
    print("\n[SETUP] conftest.py: connecting shared gateway (once for all files)")
    gateway = PaymentGateway()
    gateway.connect(api_key="SECRET_AUTH_KEY_99X")
    yield gateway
    print("\n[TEARDOWN] conftest.py: closing shared gateway")
    gateway.close()
