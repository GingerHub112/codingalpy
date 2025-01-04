import random

number = random.randint(0, 9)
count = 0
guess = 0

while True:
    if count < 3:
        pass
    else:
        print("You will never guess that the number is:", number)
        print("OOPS!")
    
    guess = int(input("What is the number? "))
    if guess == number:
        print("YAY! the number was:", number)
        break
    else:
        print("Sorry!")
        count += 1