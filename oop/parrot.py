class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = Parrot("Blue", 2)
millow = Parrot("Millow", 5)

print("Blue is a {}".format(blue.species))
print("Millow is a {}".format(millow.species))

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(millow.name, millow.age))