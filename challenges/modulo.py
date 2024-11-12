numerator = int(input("Enter a number (numerator) "))
denominator = int(input("Enter a number (denominator) "))

if(numerator % denominator == 0):
    print(numerator, "is divisible by", denominator)
else:
    print(numerator, "is not divisible by", denominator)