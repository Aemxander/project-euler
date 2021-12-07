from sieve import *

# runtime of sumPrimesBelow(2000000, 5000) is 217.033s

# sum all primes below a number N
def sumPrimesBelow(N, windowSize):
    # list of primes from sieve of eratosthenes
    primes = []
    # keep track of max prime
    maxPrime = 0

    # starting windowEnd
    windowEnd = windowSize

    # while largest prime is less than N
    while maxPrime < N:
        # set/increment windowStart
        windowStart = windowEnd - (windowSize - 1)

        # add new primes to primes list
        primes.extend(slidingSieveOfEratosthenes(windowStart, windowEnd, primes))

        # set max prime to largest prime in primes list (last number)
        maxPrime = primes[-1]

        # increment windowEnd
        windowEnd += windowSize

    # sum for all primes below N
    primesSum = 0

    # for every prime in prime list
    for prime in primes:
        # update sum if prime is below N
        if prime < N:
            primesSum += prime

    # return sum of all primes below N
    return primesSum
