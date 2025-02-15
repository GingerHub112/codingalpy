class Vehicule:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        self.fare = self.capacity * 100
        return self.fare + (self.fare / 10)
    
class Bus(Vehicule):
    def __init__(self):
        super().__init__(50)

print("Bus fare:", Bus().calculate_fare()) # Bus fare: 5500.0
