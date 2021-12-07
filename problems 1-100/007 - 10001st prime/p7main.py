from sieve import *

# runtime of findNthPrime(10001, 5000) is 11.771s

# finds the Nth prime
def findNthPrime(nthPrime, windowSize):
    # list of primes from sieve of eratosthenes
    primes = []

    # starting windowEnd
    windowEnd = windowSize

    # while you haven't reached/passed N primes
    while len(primes) < nthPrime:
        # set/increment windowStart
        windowStart = windowEnd - (windowSize - 1)

        # add new primes to primes list
        primes.extend(slidingSieveOfEratosthenes(windowStart, windowEnd, primes))

        # increment windowEnd
        windowEnd += windowSize

    # return Nth prime
    return primes[nthPrime - 1]
