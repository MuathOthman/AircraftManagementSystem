class Aircraft:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = int(capacity)
        self.passengers = []

    def board_passenger(self, passenger: str) -> bool:
        passenger = (passenger or "").strip()
        if not passenger:
            return False

        if len(self.passengers) < self.capacity:
            if passenger.upper() not in self.passengers:
                self.passengers.append(passenger.upper())
            return True
        return False

    def passenger_count(self) -> int:
        return len(self.passengers)

    def clear_passengers(self):
        self.passengers.clear()