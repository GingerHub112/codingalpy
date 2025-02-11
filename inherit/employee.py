class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("My name is {}, and my id number is {}".format(self.name, self.id))

class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.name = name
        self.id = id
        self.salary = salary
        self.post = post

a = Employee("Juan", 20335, 365, "IT vice-head")
a.display()