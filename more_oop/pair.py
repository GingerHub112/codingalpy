class pair:
    def two_sum(self, numbers, target):
        lookup = {}

        for i, x in enumerate(numbers):
            if target - x in lookup:
                return(lookup[target - x], i)
            lookup[x] = i

value = int(input("Enter a number: "))
print("index1=%d, index2=%d" % pair().two_sum((10, 20, 30, 40, 50, 60, 70, 80), value))