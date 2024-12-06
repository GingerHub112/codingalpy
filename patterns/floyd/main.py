print("Welcome to PATTERNS!")
print("------------------------------------")
print("PATTERNS: Floyd's number Pyramid")
print("")
rows = int(input("How many rows? "))
count = 0

for i in range(0, rows):
    for j in  range(i + 1):
        count = count + 1
        print(count, end=" ")

    print()