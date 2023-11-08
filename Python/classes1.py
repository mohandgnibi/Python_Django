class Flight():
    """Create a class"""

    def __init__(self, capacity):
        """Initialize the attribute."""
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        """Adding passenger to available seats."""
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        """Check the available seats"""
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
