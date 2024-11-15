mc = input("Does the student have a medical cause? [Y/N] ")
att = int(input("Enter the attendance of the student "))
if (mc == "y" or mc == "Y"):
    print("Allowed")
else:
    if (att >= 75):
        print("Allowed")
    else:
        print("Not allowed")
