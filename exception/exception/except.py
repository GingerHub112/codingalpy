try:
    x = int(input("Enter a integer: "))
except:
    print("We are sorry. An unknown error occured.")
    ret = -1
else:
    print(x)
    ret = 0
finally:
    print("Operation finished with value", ret)