while(True):
    x = int(input("Number #1 "))
    y = int(input("Number #2 "))

    print(x + y)

    z = input("Another calculation? [Y/N]")

    if(z[0] == "y" or z[0] == "Y"):
        pass
    else:
        break