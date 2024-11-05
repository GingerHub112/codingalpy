# Ask user for height and weight
height = float(input("Your height in Ms"))
weight = float(input("Your weight in KGs"))
bmi = weight/height**2

if (bmi < 18.5):
    print("You are underweight")
elif (bmi < 25):
    print("You are healthy")
elif (bmi < 30):
    print("You are overweight")
elif (bmi < 35):
    print("You are SEVERELY overweight!")
elif (bmi < 40):
    print("You are fat!!")
elif (bmi < 45):
    print("You are OBESE!!!")
else:
    print("MEDICAL CARE REQUIRED!!!!!!!!!!!!!!!!!!!")