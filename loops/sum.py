sum = int(input("Which number's sum do you want to know? "))
x = 0

for i in range(0, sum + 1):
    x += i

print("Sum of ", sum, "is:", x)