strings = input("Enter something: ")
for i in strings:
    if (i == "A" or i == "a"):
        print("A was found in the string!")
        break
    else:
        print("A not found :'(")