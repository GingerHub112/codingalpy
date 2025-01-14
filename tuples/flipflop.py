def palindrome(t):
    e = len(t) -1
    s = 0
    while s < e:
        if t[e] != t[s]:
            return False
        s+=1
        e-=1
    return True

r = (4, 5, 7, 7, 5, 4)

if(palindrome(r) == True):
    print("The tulpe is flip-flop")
else:
    print("The tulpe is flip-flop")

