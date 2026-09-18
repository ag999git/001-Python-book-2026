# payment_gateway.py
"""
Module: payment_gateway
Description: Simulates a slow, third-party payment gateway (such as Stripe or
             PayPal) so that we can see how pytest fixture scopes save time.
             No real network or money is involved.
"""

import time


class PaymentGateway:

    # Step 1 - Start in a "not connected" state
    def __init__(self):
        self.is_connected = False
        self.api_key = None

    # Step 2 - Connect to the gateway (the slow, expensive part)
    def connect(self, api_key: str):
        """
        Simulates the login ("handshake") with a remote payment server.
        With a real gateway this usually takes 1 to 3 seconds.
        Here, time.sleep(1) makes the program wait for 1 second
        so that we can feel the cost of connecting.
        """
        print(f"\n[APP] Authenticating with API Key: {api_key}... (Simulated Latency)")
        time.sleep(1)
        self.is_connected = True
        self.api_key = api_key

    # Step 3 - Close the connection
    def close(self):
        """Simulates closing the network connection cleanly."""
        print("\n[APP] Terminating network connection safely...")
        self.is_connected = False

    # Step 4 - Process a payment (only allowed while connected)
    def process_payment(self, amount: float) -> str:
        """
        The main job of the gateway. It first checks that there is an
        active connection. If not, it refuses to continue by raising an error.
        """
        if not self.is_connected:
            raise ConnectionError("Transaction Failed: Gateway connection is not established!")

        return f"Payment of ${amount:.2f} Processed Successfully."
