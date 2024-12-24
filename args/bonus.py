import math

def fun(num):
    if num % 2 == 0:
        return math.sqrt(num)
    else:
        return num ** 3

print(fun(int(input("Enter a number: "))))

def fun2(mark1, mark2, mark3, mark4, mark5):
    return f"{(mark1 + mark2 + mark3 + mark4 + mark5) / 5}%"

one = int(input("Mark of Student 1 (from 0 to 100)"))
two = int(input("Mark of Student 2 (from 0 to 100)"))
three = int(input("Mark of Student 3 (from 0 to 100)"))
four = int(input("Mark of Student 4 (from 0 to 100)"))
five = int(input("Mark of Student 5 (from 0 to 100)"))

print(fun2(one, two, three, four, five))