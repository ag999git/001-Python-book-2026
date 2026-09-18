# test_refunds.py
# This second file uses the SAME gateway object as test_orders.py.

def test_refund_payment(shared_gateway):
    print("\n   [REFUNDS] Processing a refund of $45.00")
    response = shared_gateway.process_payment(45.00)
    assert "Successfully" in response


def test_refund_gateway_is_connected(shared_gateway):
    print("\n   [REFUNDS] Checking the connection")
    assert shared_gateway.is_connected is True
