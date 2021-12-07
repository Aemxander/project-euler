import math

# sliding sieve of eratosthenes
# takes windowStart, windowEnd (included), and a list of all previous primes
# returns list of new primes from the window
def slidingSieveOfEratosthenes(windowSizeStart, windowSizeClose, primeList):
    # if not first window
    if windowSizeStart != 1:
        # create a list of numbers from windowStart to windowEnd(included)
        numberList = list(range(windowSizeStart, windowSizeClose + 1))
    # if first window - do not add 1 to list
    else:
        # create a list of numbers from 2 to windowEnd(included)
        numberList = list(range(windowSizeStart + 1, windowSizeClose + 1))

    # if not first window
    if len(primeList) >= 1:
        # for all previous primes
        for prime in primeList:
            # if potentional multiples are above the window range
            if math.ceil(windowSizeStart / prime) * prime > windowSizeClose:
                # do not search for multiples
                pass
            # if potentional multiples are within the window range
            else:
                # set number to first multiple
                currentNumber = math.ceil(windowSizeStart / prime) * prime

                # remove multiple if in list (non-prime)
                if currentNumber in numberList:
                    numberList.remove(currentNumber)

                # while next increment is within window
                while currentNumber + prime <= windowSizeClose:
                    # increment number
                    currentNumber += prime
                    # remove multiple if in list (non-prime)
                    if currentNumber in numberList:
                        numberList.remove(currentNumber)

    # if first window
    for number in numberList:
        # if no multiples of number in list
        if number * 2 > windowSizeClose:
            # do not search for multiples
            pass
        # if multiples of number in list
        else:
            # set number to 2 * number
            currentNumber = number * 2

            # remove multiple if in list (non-prime)
            if currentNumber in numberList:
                numberList.remove(currentNumber)

            # while next increment is within window
            while currentNumber + number <= windowSizeClose:
                # increment number
                currentNumber += number
                # remove multiple if in list (non-prime)
                if currentNumber in numberList:
                    numberList.remove(currentNumber)

    # return list of new primes from the window
    return numberList
