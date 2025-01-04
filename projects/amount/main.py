x = int(input("What is the total amount of the bill? "))
y = int(input("How much you paid? "))
z = x - y

def calculate():
    return f"You need to pay {z} more."

print(calculate())