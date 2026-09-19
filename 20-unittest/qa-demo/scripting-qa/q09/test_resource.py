# test_resource.py
# Run it with:  pytest -v -s test_resource.py

import pytest


class Resource:

    def start(self):
        print("[APP] resource started")

    def stop(self):
        print("[APP] resource stopped")


@pytest.fixture
def resource():

    # Step 1: Setup section
    print("\n[FIXTURE] setup")
    obj = Resource()
    obj.start()

    # Step 2: Send the object to the test
    yield obj

    # Step 3: Teardown section (runs after the test finishes, even if it fails)
    print("\n[FIXTURE] teardown")
    obj.stop()


def test_resource(resource):

    # Step 4: resource holds the object sent by yield
    print("[TEST] running")
    assert isinstance(resource, Resource)
