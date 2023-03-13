# Quiz 50
## Solution
```.py
class flight_offered():
    def __init__(self, flight_number, origin, destination, departure_time, duration):
        self.flight_number = flight_number
        self.origin = origin
        self.destination: destination
        self.departure_time = departure_time
        self.duration = duration

    def get_duration(self):
        hours, minutes, seconds = self.duration
        return f"{hours} hours {minutes} minutes and {seconds} seconds"
```

## Test
```.py
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
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_050_result.png)

**Fig.1** Evidence for quiz 50
