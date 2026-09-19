# test_q06_fixture_yield.py - Question 6: setup and teardown with yield
# Run it with:  pytest -v -s test_q06_fixture_yield.py

import pytest


@pytest.fixture
def resource():
    # Step 1 - Setup: runs before the test
    print("\n   [setup] creating the resource")
    obj = {"status": "open"}

    # Step 2 - Hand the resource to the test
    yield obj

    # Step 3 - Teardown: runs after the test, even if it fails
    obj["status"] = "closed"
    print("\n   [teardown] resource closed")


def test_resource_is_open(resource):
    print("   [test] using the resource")
    assert resource["status"] == "open"
