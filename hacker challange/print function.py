def printFunction(n):
    if n == 0:
        return
    printFunction(n-1)

    print(n, end='')

n = int(input())
printFunction(n)