tmp = ()
while True:
    print(tmp)
    z = input("Enter a option (A)ppend to tulpe or E(X)ecute program: ")
    if z == "A" or z == "a":
        z = input("Append what? ")
        confirm = input("Are you SURE? (Y/N): ")
        if confirm == "Y" or confirm == "y":
                        tmp2 = (z,)
                        tmp = tmp + tmp2
    elif z == "X" or z == "x":
        break

mul = 1
for i in tmp:
    mul = mul * int(i)
    

print("Product of the tulpe:", mul)