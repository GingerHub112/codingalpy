class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def _fuel_type(self):
        print("BMW's fuel type is", self.fuel_type)

    def _max_speed(self):
        print("BMW's maximum speed is", self.max_speed)

    def move(self, speed):
        if speed <= self.max_speed:
            print("BMW has moved with a speed of", speed, "KM per hour")
        else:
            print("The car can't go that fast!")

class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def _fuel_type(self):
        print("Ferrari's fuel type is", self.fuel_type)

    def _max_speed(self):
        print("Ferrari's maximum speed is", self.max_speed)

    def move(self, speed):
        if speed <= self.max_speed:
            print("Ferrari has moved with a speed of", speed, "KM per hour")
        else:
            print("The car can't go that fast!") 

f = Ferrari("Gasoline", 260)
b = BMW("Diesel", 340)
f._fuel_type()
b._fuel_type()
f._max_speed()
b._max_speed()
f.move(70)
b.move(400)