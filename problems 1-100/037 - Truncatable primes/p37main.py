from sieve import *
from truncation import *

# runtime of sumLeftAndRightTruncatablePrimes(5000) is 130.415s

# find and sum the 11 left and right truncatable primes
def sumLeftAndRightTruncatablePrimes(windowSize):
    # list of primes from sieve of eratosthenes
    primes = []

    # count and sum for truncatable primes
    truncatablePrimeCount = 0
    truncatablePrimeSum = 0

    # starting windowEnd
    windowEnd = windowSize

    # problem states there are exactly 11 left and right truncatable primes
    while truncatablePrimeCount != 11:
        # set/increment windowStart
        windowStart = windowEnd - (windowSize - 1)

        # new primes from sieve of eratosthenes window
        newSieveResults = slidingSieveOfEratosthenes(windowStart, windowEnd, primes)

        # add new primes to prime list
        primes.extend(newSieveResults)

        # for all new primes from sieve of eratosthenes window
        for prime in newSieveResults:
            # only look for truncatable primes >= 10
            if prime >= 10:

                # increment count and sum if left and right truncatable
                if checkIfLeftRightTruncatablePrime(prime, primes) == True:
                    truncatablePrimeCount += 1
                    truncatablePrimeSum += prime

        # increment windowEnd
        windowEnd += windowSize

    # return sum of 11 left and right truncatable primes
    return truncatablePrimeSum
