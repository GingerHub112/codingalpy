def cube(num):
    return num ** 3

def byThree(num):
    if(num % 3 == 0):
        return cube(num)
    else:
        return False
    
print(byThree(6))
print(byThree(9))