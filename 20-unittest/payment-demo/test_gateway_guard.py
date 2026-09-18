# test_gateway_guard.py
"""
Checks the defensive guard in process_payment():
a gateway that was never connected must refuse to take a payment.
Run using 'pytest -v -s test_gateway_guard.py'.
"""

# Step 1 - Import pytest and the class we want to test
import pytest
from payment_gateway import PaymentGateway


def test_payment_without_connection_is_refused():
    # Step 2 - Create a gateway but do NOT connect it.
    #          No fixture is needed, and no slow connection is made.
    gateway = PaymentGateway()
    print("\n   Gateway created. is_connected =", gateway.is_connected)

    # Step 3 - pytest.raises passes only if the code inside
    #          the 'with' block raises ConnectionError
    with pytest.raises(ConnectionError) as error_info:
        gateway.process_payment(50.00)

    # Step 4 - Show and check the error message
    print("   Error raised:", error_info.value)
    assert "not established" in str(error_info.value)
