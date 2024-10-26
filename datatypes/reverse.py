# Ask for string
str = input("Write something...")

#Reverse algoritm

print("Processing")
reverse = ""

while (len(str) > 0):
    reverse = str[0] + reverse
    str = str[1 : len(str)]

#Returns reversed string
print("Finished processing!")
print("Exits with return:", reverse)
