# test_q16_skip_xfail.py - Question 16: skip vs xfail
# Run it with:  pytest -v -rsxX test_q16_skip_xfail.py
# (-rsxX asks pytest to list the reasons for skipped, xfailed and xpassed tests)

import pytest
from calculator import add_buggy, add


# Step 1 - skip: the test is NOT run at all
@pytest.mark.skip(reason="feature not available yet")
def test_export_to_pdf():
    assert False   # never runs


# Step 2 - xfail: the test IS run; failing is expected because of a known bug
@pytest.mark.xfail(reason="known bug: add_buggy adds 1 too many")
def test_known_bug():
    assert add_buggy(2, 2) == 4


# Step 3 - xfail on a test that actually passes is reported as XPASS
@pytest.mark.xfail(reason="bug thought to exist, but it is fixed")
def test_bug_already_fixed():
    assert add(2, 2) == 4
