import math

# find all factors pairs for a number N
def findFactorPairs(N):
    # create a list for factor pairs
    factorPairList = []

    # search for factors in decreasing order
    for i in range(int(math.sqrt(N))+1, 0, -1):
        # append factor pair to factor pair list
        if N % i == 0:
            factorPairList.append([i, int(N / i)])

    # return a list of factor pairs (lists)
    return factorPairList
