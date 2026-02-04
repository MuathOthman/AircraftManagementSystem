class Aircraft:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = int(capacity)
        self.passengers = []

    def board_passenger(self, passenger: str) -> bool:
        """Boards passenger if capacity allows. Returns True if boarded, else False."""
        passenger = (passenger or "").strip()
        if not passenger:
            return False

        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def passenger_count(self) -> int:
        return len(self.passengers)

