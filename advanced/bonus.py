import math

i1 = [1, 3, 5, 7, 9]
i2 = [2, 4, 6, 8, 10, 11]

zipi = list(zip(i1, i2))
print(zipi)

lists = [2, 3, 4, 5]
def cube(x):
    return x**3
print(list(map(cube, lists)))

odd = [i for i in i2 if i%2!=0]
even = [i for i in i2 if i%2==0]
print(odd)
print(even)