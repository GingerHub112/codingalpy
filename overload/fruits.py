import random

class FruitQuiz():
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "orange": "orange",
            "banana": "yellow",
            "watermelon": "green"
        }

    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}?".format(fruit), end=" ")
            anwser = input()
            if(anwser.lower() == color):
                print("CORRECT!")
            else:
                print("NUH UH!")
            
            x = input("Want to play again (Y/N)? ")

            if(x == "Y" or x == "y"):
                continue
            else:
                break

print("Fruit Quiz")
fruitq = FruitQuiz()
fruitq.quiz()