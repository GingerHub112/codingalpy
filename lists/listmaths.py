x = True
l = []
while x:
    print(l)
    answer = input("Enter a option: (A)ppend a number to list, (P)op element from list, E(x)ecute the program ")
    if(answer == "A" or answer == "a"):
        try:
            answer = int(input("Enter a integer: "))
        except ValueError:
            print("Value is not integer!")
            continue
        else:
            l.append(answer)
    elif(answer == "p" or answer == "P"):
        try:
            answer = int(input("Enter which element to pop "))
            l.remove(answer)
        except ValueError:
            print("Value is not integer!")
            continue
        except IndexError:
            print("Value is out of range!")
            continue
    elif(answer == "x" or answer == "X"):
        break

tmp = 0
for i in l:
    tmp = i + tmp

print("Sum of list is", tmp)
print("Average of list is", tmp/len(l))
print("Largest element of list is", max(l), "and the smallest element is", min(l))