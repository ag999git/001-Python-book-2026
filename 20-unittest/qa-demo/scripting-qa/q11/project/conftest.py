# conftest.py
# Fixtures in this file are shared with every test file in this folder
# (and in the folders inside it). Test files do not import them.

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():

    # Step 2: Create the object
    print("\n[FIXTURE] creating calculator")
    obj = Calculator()

    # Step 3: Return the object to the test
    return obj
