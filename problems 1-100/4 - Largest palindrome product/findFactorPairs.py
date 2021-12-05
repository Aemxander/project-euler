import math

# find all factors pairs for a number N
def findFactorPairs(inputNumber):
    # create a list for factor pairs
    factorPairList = []

    # search for factors in decreasing order
    for i in range(int(math.sqrt(inputNumber))+1, 0, -1):
        # append factor pair to factor pair list
        if inputNumber % i == 0:
            factorPairList.append([i, int(inputNumber / i)])

    # return a list of factor pairs (lists)
    return factorPairList
