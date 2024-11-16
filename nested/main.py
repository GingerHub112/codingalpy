print("Choose a option: 1. Bike, 2. Car ")
x = int(input(""))

if(x == 1):
    print("You chose a bike! Now choose between 1. Scooty, 2. Scooter ")
    x = int(input(""))
    if(x == 1):
        print("Scooty was chosen!")
    elif (x == 2):
        print("Scooter was chosen!")
    else:
        print("I don't understand")
        print("ERROR: Value was outside of range")
elif (x == 2):
    print("You chose a car! Now choose between 1. Sedan, 2. XUV ")
    x = int(input(""))
    if(x == 1):
        print("Sedan was chosen!")
    elif (x == 2):
        print("XUV was chosen!")
    else:
        print("I don't understand")
        print("ERROR: Value was outside of range")
else:
    print("I don't understand")
    print("ERROR: Value was outside of range")
