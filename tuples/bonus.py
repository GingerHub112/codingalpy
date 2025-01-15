tmp = ()
while True:
    print(tmp)
    z = input("Enter a option (A)ppend to list or S(o)rt odd and even: ")
    if z == "A" or z == "a":
        z = input("Append what? ")
        confirm = input("Are you SURE? (Y/N): ")
        if confirm == "Y" or confirm == "y":
            confirm = input("Are you SURE SURE? (Y/N): ")
            if confirm == "Y" or confirm == "y":
                confirm = input("Are you SURE SURE SURE? (Y/N): ")
                if confirm == "Y" or confirm == "y":
                    confirm = input("THIS IS PERMANENT!!! (Y/N): ")
                    if confirm == "Y" or confirm == "y":
                        tmp2 = (z,)
                        tmp = tmp + tmp2
    elif z == "O" or z == "o":
        break

odd = ()
even = ()
for i in tmp:
    if int(i) % 2 == 0:
        tmp2 = (i,)
        even = even + tmp2
    else:
        tmp2 = (i,)
        odd = odd + tmp2

print(odd)
print(even)