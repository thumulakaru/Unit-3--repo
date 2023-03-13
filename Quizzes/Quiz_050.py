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
