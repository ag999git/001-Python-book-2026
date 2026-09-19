# test_session.py
# Run it with:  pytest -v -s test_session.py

import pytest

# Counts how many times the fixture's setup runs
count = 0


class Connection:

    def connect(self):
        print("[APP] connecting")

    def close(self):
        print("[APP] closing")


@pytest.fixture(scope="session")
def connection():

    # 'global' lets the fixture change the count defined above
    global count

    # Step 1: This part runs only once for the whole session
    count += 1
    print(f"\n[FIXTURE] setup count = {count}")
    obj = Connection()
    obj.connect()

    # Step 2: Provide the same object to all tests
    yield obj

    # Step 3: Clean up at the end of the session
    print()
    obj.close()


def test_one(connection):
    print(f"[TEST] one (count = {count})")
    assert isinstance(connection, Connection)


def test_two(connection):
    print(f"[TEST] two (count = {count})")
    assert isinstance(connection, Connection)


def test_three(connection):
    print(f"[TEST] three (count = {count})")
    assert isinstance(connection, Connection)
