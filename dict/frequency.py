dictionnary = {"A": 2, "value": 2, "can": 2, "be": 2, "a": 1, "string": 1, "int": 1, "or": 1, "float": 1}
def frequency(dictionnarylist , times):
    count = 0
    for key in dictionnary:
        if dictionnarylist[key] == times:
            count += 1
    return count

print("The amount of 2s in our dictionary is:", frequency(dictionnary, 2))
