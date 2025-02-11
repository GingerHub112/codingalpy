class Bird:
    def __init__(self, name):
        self.name = name
        print("Bird is ready!")

    def mySpecies(self):
        print("I am a bird!")

    def myName(self):
        print("My name is:", self.name)

    def swim(self):
        print("Bird is swimming!")

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)
        print("Penguin is ready")

    def mySpecies(self):
        print("I am a penguin!")

    def run(self):
        print("Penguin is swimming!")

tux = Penguin("Tux")
peggy = Penguin("Peggy")
tux.mySpecies()
peggy.swim()
tux.run()