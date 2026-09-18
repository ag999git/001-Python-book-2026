# test_payments_function_scope.py
"""
The same three tests as test_payments.py, but the fixture uses the
default function scope. Compare the output and the total time.
Run using 'pytest -v -s test_payments_function_scope.py'.
"""

# Step 1 - Import pytest and the class we want to test
import pytest
from payment_gateway import PaymentGateway

# Step 2 - Counter to show how many times the fixture runs
FUNCTION_FIXTURE_INSTANTIATIONS = 0


# Step 3 - A function-scoped fixture (scope="function" is the default,
#          so writing @pytest.fixture alone would do the same thing)
@pytest.fixture(scope="function")
def gateway_function():
    global FUNCTION_FIXTURE_INSTANTIATIONS
    FUNCTION_FIXTURE_INSTANTIATIONS += 1
    print(f"\n[SETUP] FUNCTION START (Initialization Count: {FUNCTION_FIXTURE_INSTANTIATIONS})")

    gateway_instance = PaymentGateway()
    gateway_instance.connect(api_key="SECRET_AUTH_KEY_99X")

    yield gateway_instance

    print(f"\n[TEARDOWN] FUNCTION END (Count so far: {FUNCTION_FIXTURE_INSTANTIATIONS})")
    gateway_instance.close()


# Step 4 - The same three tests, now using the function-scoped fixture

def test_low_value_transaction(gateway_function):
    response = gateway_function.process_payment(15.50)
    assert "Successfully" in response


def test_high_value_transaction(gateway_function):
    response = gateway_function.process_payment(7500.00)
    assert "Successfully" in response


def test_gateway_persistence(gateway_function):
    assert gateway_function.is_connected is True
