import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
my_circle = circle(2.4)
print("Radius of my circle is {}, the area of my circle is {} and the perimeter of my circle is {}.".format(my_circle.radius, my_circle.area(), my_circle.perimeter()))