anwser = int(input("Enter a number: "))
evens = [x for x in range(anwser) if x % 2 == 0]
odds = [x for x in range(anwser) if x % 2 != 0]
print(evens)
print(odds)
squares = [x.title() for x in ("apples", "bananas", "oranges")]