def printToN(n):
    if n <= 0:
        return 0
    else:
        printToN(n-1)
        print(n)

printToN(10)
