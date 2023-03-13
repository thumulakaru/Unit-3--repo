import pytest
from Quiz_050 import flight_offered


def test_get_duration():
    # Create an instance of class Flights
    flight = flight_offered('QF456', 'SFO', 'SYD', '6:00pm', [7, 25, 5])

    # Assert the output of get_duration()
    assert flight.get_duration() == "7 hours 25 minutes and 5 seconds"


def test_get_duration_2():
    flight = flight_offered('UL454', 'CMB', 'NRT', "7.30am", [9, 30, 00])

    assert flight.get_duration() == "9 hours 30 minutes and 0 seconds"
