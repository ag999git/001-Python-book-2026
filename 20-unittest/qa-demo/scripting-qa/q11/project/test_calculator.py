# test_calculator.py
# Run it with:  pytest -v -s test_calculator.py
# Notice: there is NO "from conftest import calculator"


def test_add(calculator):

    # Step 1: The calculator object is injected automatically
    print("[TEST] add started")
    result = calculator.add(5, 10)

    # Step 2: Check the result
    assert result == 15
