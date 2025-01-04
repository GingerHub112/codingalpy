import random

possible = ["rock", "paper", "scissors"]
cpu = possible[random.randint(0,2)]
player = input("Enter a option (rock, paper, scissors): ")
print("Player chose:", player, "and the CPU chose", cpu)

if player == cpu:
    print("Its a tie!")
elif player == "rock":
    if cpu == "paper":
        print("CPU wins!")
    else:
        print("Player wins!")
elif player == "paper":
    if cpu == "scissors":
        print("CPU wins!")
    else:
        print("Player wins!")
elif player == "scissors":
    if cpu == "rock":
        print("CPU wins!")
    else:
        print("Player wins!")
else:
    print("The game coudn't be played correctly")