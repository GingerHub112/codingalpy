class Dog:
    animal = "dog"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Browny", "German Shepard")
dog2 = Dog("Fuzzy", "Poodle")

print("{} is a {} with a breed of {}".format(dog1.name, dog1.animal, dog1.breed))
print("{} is a {} with a breed of {}".format(dog2.name, dog2.animal, dog2.breed))