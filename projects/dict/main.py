dictionnary = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
def frequency(dictionnarylist , times):
    count = 0
    for key in dictionnary:
        if dictionnarylist[key] == times:
            count += 1
    return count

i = int(input("Enter the value of which element you want to calculate the frequency of: "))
print(frequency(dictionnary, i))

