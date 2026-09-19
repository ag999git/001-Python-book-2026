# test_q10_mock.py - Questions 10 and 11: replacing a slow service with a Mock
# Run it with:  pytest -v -s test_q10_mock.py

from unittest.mock import Mock


# Step 1 - The code under test: it asks a weather service for a temperature
def weather_message(service):
    temperature = service.get_temperature("Ranchi")
    if temperature > 35:
        return "Hot day"
    return "Pleasant day"


# Step 2 - A test that uses a Mock instead of a real internet service
def test_hot_day():
    fake_service = Mock()
    fake_service.get_temperature.return_value = 40   # we choose the answer

    message = weather_message(fake_service)
    print(f"\n   message = {message!r}")

    assert message == "Hot day"
    # The mock also records how it was used
    fake_service.get_temperature.assert_called_once_with("Ranchi")
