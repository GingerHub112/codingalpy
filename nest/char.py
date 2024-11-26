word = input("Enter a string ")
char = input("Enter a character ")
count = 0

for i in word:
    if char == i:
        count += 1

print("Char found in string (number):", count)