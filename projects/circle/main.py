import math

def circumeference(diameter):
    return diameter * math.pi

d = int(input("Enter diameter of circle: "))
print("The circumference of the circle is around:", circumeference(d))