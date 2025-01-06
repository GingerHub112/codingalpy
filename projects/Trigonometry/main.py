import math

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("You entered a non-integer value!")
except KeyboardInterrupt:
    print("You pressed Ctrl-C!")
else:
    print(math.cos(x))
    print(math.sin(x))
    print(math.tan(x))