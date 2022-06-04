def printNos(N):
        if N == 0:
            return
        else:
            printNos(N-1)
            print(N)

printNos(100
)