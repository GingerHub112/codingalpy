# Up to 5 grades: Science, English, Spanish, Maths and French, though they can be used for other purposes
sci = int(input("What is your science grade?"))
maths = int(input("What is your maths grade?"))
eng = int(input("What is your English grade?"))
french = int(input("What is your French grade?"))
spanish = int(input("What is your Spanish grade?"))

#Sum up all these grades, then divide them by 500, then multiply them by 100
print("You average in grades:", (sci + maths + eng + french + spanish)/500*100)