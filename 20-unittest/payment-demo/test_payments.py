# test_payments.py
"""
Suite: test_payments
Description: Shows how a session-scoped fixture creates and connects the
             PaymentGateway only once, and shares it with every test.
Execution Note: Run using 'pytest -v -s test_payments.py'.
                The -s flag turns off output capturing, so the print()
                messages from the fixture and the tests appear on the screen.
"""

# Step 1 - Import pytest and the class we want to test
import pytest
from payment_gateway import PaymentGateway

# Step 2 - A counter that records how many times the fixture runs.
# It is used only for teaching, to prove how often setup happens.
SESSION_FIXTURE_INSTANTIATIONS = 0


# Step 3 - The session-scoped fixture
@pytest.fixture(scope="session")
def gateway_session():
    """
    Session-scoped fixture. It creates, connects and later closes the
    PaymentGateway exactly once for the whole test run, no matter how
    many tests ask for it.
    """
    # 'global' lets this function change the counter defined outside it
    global SESSION_FIXTURE_INSTANTIATIONS
    SESSION_FIXTURE_INSTANTIATIONS += 1

    print(f"\n[SETUP] GLOBAL SESSION START (Initialization Count: {SESSION_FIXTURE_INSTANTIATIONS})")

    # Setup phase: create the gateway and connect (the slow part)
    gateway_instance = PaymentGateway()
    gateway_instance.connect(api_key="SECRET_AUTH_KEY_99X")

    # Hand the connected gateway to every test that asks for it.
    # The fixture pauses here until the last test in the session has finished.
    yield gateway_instance

    # Teardown phase: runs once, after the last test in the session
    print(f"\n[TEARDOWN] GLOBAL SESSION END (Final Verification Count: {SESSION_FIXTURE_INSTANTIATIONS})")
    gateway_instance.close()


# Step 4 - The tests. Each one asks for 'gateway_session' by name.

def test_low_value_transaction(gateway_session):
    """Checks that the gateway can process a small, normal payment."""
    print("\n   [TEST 1] Dispatching $15.50 payment payload...")
    response = gateway_session.process_payment(15.50)
    assert "Successfully" in response
    print("   [TEST 1] Assertion Verified Successfully.")


def test_high_value_transaction(gateway_session):
    """Checks that the gateway can process a large payment."""
    print("\n   [TEST 2] Dispatching $7500.00 payment payload...")
    response = gateway_session.process_payment(7500.00)
    assert "Successfully" in response
    print("   [TEST 2] Assertion Verified Successfully.")


def test_gateway_persistence(gateway_session):
    """Checks that the same connection is still open after the earlier tests."""
    print("\n   [TEST 3] Auditing state persistence of active network socket...")
    assert gateway_session.is_connected is True
    print("   [TEST 3] Assertion Verified: State Persistence Confirmed.")
