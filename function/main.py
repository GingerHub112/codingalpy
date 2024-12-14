def add(i, x):
    return i + x
def subtract(i, x):
    return i - x
def multiply(i, x):
    return i * x
def divide(i, x):
    return i / x
def remainder(i, x):
    return i % x

print("Here are options:")
print("a : Addition")
print("b : Subtraction")
print("c : Multiplication")
print("d : Division")
print("e : Remainder (aka. Modulus)")

choice = input("Enter your option: ")
a = ""
b = ""

if (choice == "a"):
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    print(add(a, b))
elif (choice == "b"):
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    print(subtract(a, b))
elif (choice == "c"):
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    print(multiply(a, b))
elif (choice == "d"):
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    print(divide(a, b))
elif (choice == "e"):
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    print(remainder(a, b))
else:
    print("I didn't understand!")