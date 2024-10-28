# Ask the amount of the notes
amt = int(input("Enter your notes here: "))

#Process score...
score2000 = amt // 2000
amt = amt % 2000
print('2000 amount of notes required: ', score2000)
score500 = amt // 500
amt = amt % 500
print('500 amount of notes required: ', score500)
score100 = amt // 100
amt = amt % 1000
print('100 amount of notes required: ', score100)
