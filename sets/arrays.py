import array as a
arr = a.array("l", [1, 2, 3])

for i in range(0,3):
    print(arr[i], end=" ")
print()

b = a.array("d", [2.5, 3.2, 3.3])

for i in range(0,3):
    print(b[i], end=" ")
print()

arr.insert(0, 4)
for i in range(1,3):
    print(arr[i], end=" ")
print()

b.append(4.4)
for i in range(0,3):
    print(b[i], end=" ")
print()