#n(n-1)

def fact(n):
    if n == 1:
        return 0
    return n*fact(n-1)

def printN(n):
    if n == 0:
        return
    printN(n - 1)
    print(n)


printN(20)
