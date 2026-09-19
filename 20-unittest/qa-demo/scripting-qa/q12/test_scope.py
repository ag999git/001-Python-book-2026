# test_scope.py
# Run it with:  pytest -v -s test_scope.py

import pytest


# Step 1: Function scope is the default scope.
#         It runs once for every test function.
@pytest.fixture(scope="function")
def function_fixture():
    print("\n[FIXTURE] function setup")
    return "object"


# Step 2: Module scope runs once per file
@pytest.fixture(scope="module")
def module_fixture():
    print("\n[FIXTURE] module setup")
    return "object"


def test_one(function_fixture, module_fixture):
    print("[TEST] one")


def test_two(function_fixture, module_fixture):
    print("[TEST] two")
