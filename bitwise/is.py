x = 50

if(type(x) is int):
    print(":-)")
else:
    print(":-(")

x = 50.0

if(type(x) is not float):
    print(":-)")
else:
    print(":-(")

x = 24
y = 24

if(x is y):
    print("x and y are the same")
else:
    print("x and y aren't the same")