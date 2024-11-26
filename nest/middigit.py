num = int(input("Enter a number "))
tmp = num
lenght = len(str(num))
if lenght >= 4:
    lenght = lenght // 2
    chk = 0
    while num > 0:
        rmdr = num % 10
        if chk == lenght:
            m1 = rmdr
        elif chk == lenght-1:
            m2 = rmdr
        num = num // 10
        chk = chk + 1
        # m1/m2 is not defined: FIXED
    product = m1 * m2
    print("The product is:", product)
else:
    print("Number should greater or equal to 4")