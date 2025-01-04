try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input")
else:
    if(age % 2 == 0):
        print("Even age")
    else:
        print("Odd age")
finally:
    pass