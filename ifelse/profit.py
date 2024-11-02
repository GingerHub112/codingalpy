op = int(input("What is the original price? "))
sp = int(input("What is the sales price? "))

profit = sp - op
loss = op - sp

if (profit > 0):
    print("You've earned a profit of:", profit)
else:
    print("You've lost a total of:", loss)