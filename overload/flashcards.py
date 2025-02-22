class flashcard():
    def __init__(self, front, back):
        self.front = front
        self.back = back
    
    def __str__(self):
        return self.front + ": " + self.back

print("FLASHCARDS")
cards = []

while True:
    x = input("Enter the front of the flashcard: ")
    y = input("Enter the back of the flashcard: ")

    tempcard = flashcard(x, y)
    cards.append(str(tempcard))
    x = input("Do you want to stop writing flash cards [Y/N]? ")
    if x == "Y" or x == "y":
        break
    else:
        continue

print("-----")
print("MY FLASH CARDS")
for i in cards:
    print(str(i))
