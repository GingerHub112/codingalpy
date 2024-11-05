a = 5
b = 2
c = 7

if (a == b and a == c):
    # Will never happen
    print("All are equal")
else:
    print(">_<")

if(a != b or a != c):
    print("I have a fact: They do NOT match ")
else:
    # Will never happen
    print("o_o")