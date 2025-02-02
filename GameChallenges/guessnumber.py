import random
rand = random.randint(1, 100)
while(True):
    i = int(input("Which number did the CPU think of (1-100): "))
    if i < rand:
        print("Your answer is less than the CPU thought of!")
    elif i > rand:
        print("Your answer is higher than the CPU thought of!")
    elif i == rand:
        print("Your answer is the same number as the CPU thought of!")
        break

