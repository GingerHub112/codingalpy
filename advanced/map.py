numbers1 = [1, 3, 5, 7]
numbers2 = [2, 4, 6, 8]
result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result)

def square1(n):
    return n*n

square = list(map(square1, numbers1))
print(square)