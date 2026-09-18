# test_contamination.py
"""
Shows the main danger of a session-scoped fixture: one test changes the
shared object, and a later test fails because of it.
Run using 'pytest -v -s test_contamination.py'.
The second test FAILS on purpose.
"""

# Step 1 - Import pytest and the class we want to test
import pytest
from payment_gateway import PaymentGateway


# Step 2 - One shared gateway for the whole session
@pytest.fixture(scope="session")
def shared_gateway():
    print("\n[SETUP] Connecting shared gateway once")
    gateway = PaymentGateway()
    gateway.connect(api_key="SECRET_AUTH_KEY_99X")
    yield gateway
    print("\n[TEARDOWN] Closing shared gateway")
    gateway.close()


# Step 3 - A test that changes the shared object.
#          It simulates a network failure by closing the connection,
#          and it does not reconnect afterwards.
def test_simulated_network_failure(shared_gateway):
    shared_gateway.close()
    print("   Connection closed by test 1. is_connected =", shared_gateway.is_connected)
    with pytest.raises(ConnectionError):
        shared_gateway.process_payment(10.00)


# Step 4 - A perfectly correct test that now fails,
#          because it receives the gateway that test 1 closed.
def test_normal_payment(shared_gateway):
    print("\n   Test 2 receives is_connected =", shared_gateway.is_connected)
    response = shared_gateway.process_payment(20.00)
    assert "Successfully" in response
