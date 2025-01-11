def matchWords(words):
    count = 0
    l = []
    for i in words:
        if (len(i) >= 2 and (i[0] == i[-1])):
            count += 1
            l.append(i)
    print("List of words with the same character, at the start and end:", l)
    return count

print("Number of words with the same character, at the start and end:", matchWords(["abc", "cfc", "xyz", "aba", "1221"]))
