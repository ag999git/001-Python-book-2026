# database.py
# This is a simple database module that simulates connecting to a database.
# No real database is used. The print() messages let us see
# exactly when each part of the code runs.


class Database:

    # Step 1 - Runs every time a new Database object is created
    def __init__(self):
        print("[DB] Database object created")

    # Step 2 - Pretends to connect to a database.
    # In a real program this would be the slow, expensive part
    # (opening a network connection, logging in, and so on).
    def connect(self):
        print("[DB] connect called")
        return "connected"

