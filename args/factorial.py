def factorial(x):
    '''Factorial function (example: factorial(5) will return the same as 5 * 4 * 3 * 2 * 1)'''

    if (x == 0 or x == 1):
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial(5))
print(factorial(10))