print("Enter your grades.")
m1 = int(input("Enter a grade! "))
m2 = int(input("Enter a grade! "))
m3 = int(input("Enter a grade! "))
m4 = int(input("Enter a grade! "))
m5 = int(input("Enter a grade! "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

if (avg >= 91 and avg <= 100):
    print("Your average is A1")
elif (avg >= 81 and avg < 91):
    print("Your average is A2")
elif (avg >= 71 and avg < 81):
    print("Your average is B1")
elif (avg >= 61 and avg < 71):
    print("Your average is B2")
elif (avg >= 51 and avg < 61):
    print("Your average is C1")
elif (avg >= 41 and avg < 51):
    print("Your average is C2")
elif (avg >= 33 and avg < 41):
    print("Your average is D")
elif (avg >= 21 and avg < 33):
    print("Your average is E1")
elif (avg >= 0 and avg < 21):
    print("Your average is E2")
else:
    print("ERROR!")