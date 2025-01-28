l1 = [1, 2, 3, 4]
l2 = [2,4,6,8]
l3 = list(zip(l1, l2))
print(l3)

for i, j in zip(l1, l2[::-1]):
    print(i, j)

dict = {l1: l2 for l1, l2 in zip(l1, l2)}
print(format(dict))