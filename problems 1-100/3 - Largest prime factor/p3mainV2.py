import math

# find the largest prime factor of N
def LargestPrimeFactor(inputNumber):
    # search for factors in decreasing order
    for i in range((math.floor(inputNumber / 2) + 1), 0, -1):

        # if a factor
        if inputNumber % i == 0:

            # check if prime
            if CheckIfPrime(i) == True:
                # return largest prime factor
                return i

    # blanket return
    return 1


# https://tacomacc.instructure.com/courses/1931063/pages/prime-number-test?module_item_id=41167387
def CheckIfPrime(inputNumber):
    # find the square root and round down
    roundedSquareRoot = math.floor(math.sqrt(inputNumber))

    # check for any factors
    for i in range(2, (roundedSquareRoot + 1)):
        # if there is a factor return false since non-prime
        if inputNumber % i == 0:
            return False

    # if there are no factors return true since prime
    return True

print(LargestPrimeFactor(600851475143))
