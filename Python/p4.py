def IsPalindrome(a):
    numberToString = str(a)
    j = len(numberToString)-1
    i = 0
    while (i < j):
        if numberToString[i] != numberToString[j]:
            return False
        i=i+1
        j=j-1
    return True

def GenerateXDigitNumbersAndCheck(a):
    i = 10**(a) #"10, 100, 1000, etc"
    x = 10**(a+1)-1 #"99, 999, 9999, etc"
    pal = []
    for a in xrange(x+1,i,-1):
        for b in xrange(x+1,a+1,-1):
            prod = a*b
            if IsPalindrome(prod):
                vpal = prod,a,b
                pal.append(vpal)
    print max(pal)

GenerateXDigitNumbersAndCheck(4)
