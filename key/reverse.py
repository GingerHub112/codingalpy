num = int(input("Enter a integer: "))
rev = 0
for i in range(0, len(str(num))):
    rem = num % 10
    rev = rev*10+rem
    num = num // 10
print(rev)