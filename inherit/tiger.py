class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.animal = "animal"

    def whoAmI(self):
        print("My name is {} and I am a {}".format(self.name, self.animal))

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.animal = "tiger"

raj = Tiger("Raj", 3)
raj.whoAmI()