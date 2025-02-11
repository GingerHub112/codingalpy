class Vehicule:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicule):
    pass

school_bus = Bus("School Volvo", 280, 12)
print("Veichule name: {}, Max Speed: {}, Mileage: {}".format(school_bus.name, school_bus.max_speed, school_bus.mileage))