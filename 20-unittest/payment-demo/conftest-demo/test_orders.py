# test_orders.py
# No import of shared_gateway is needed. Pytest finds it in conftest.py.

def test_order_payment(shared_gateway):
    print("\n   [ORDERS] Paying for an order of $120.00")
    response = shared_gateway.process_payment(120.00)
    assert "Successfully" in response


def test_order_gateway_is_connected(shared_gateway):
    print("\n   [ORDERS] Checking the connection")
    assert shared_gateway.is_connected is True
