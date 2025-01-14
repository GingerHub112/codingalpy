from_ = int(input("Enter a number: "))
to_ = int(input("Enter an other number: "))
odd = []
even = []
for i in range(from_, to_):
    if i ** 2 % 2 == 0:
        even.append(i ** 2)
    else:
        odd.append(i ** 2)

print("Odd:", odd)
print("Even:", even)