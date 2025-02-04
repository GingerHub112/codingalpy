class vehicule:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car_model = vehicule(180, 16)
print("Car's maximum speed:", car_model.max_speed)
print("Car's mileage:", car_model.mileage)