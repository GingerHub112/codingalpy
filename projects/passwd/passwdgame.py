import random

string = ""
abcs = "abcdefghijklmnopqrstuvwxyz"
special = "@!\"#$%&/()=?_-"
for i in range(0, random.randint(8, 11)):
    x = random.randint(1, 4)
    if x == 1:
        string = string + random.choice(abcs)
    elif x == 2:
        string = string + str(random.randint(0, 9))
    elif x == 3:
        string = string + random.choice(special)
    elif x == 4:
        string = string + random.choice(abcs.upper())

print(string)