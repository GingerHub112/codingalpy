for x in range(0, 100):
    if(x % 20 == 0):
        print("TWIST")
    elif(x % 15 == 0):
        pass #NULL
    elif(x % 5 == 0):
        print("FIZZ")
    elif(x % 3 == 0):
        print("BUZZ")
    else:
        print(x)