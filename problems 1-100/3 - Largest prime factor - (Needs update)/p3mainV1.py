import math

# find the largest prime factor of N
def LargestPrimeFactor(inputNumber):

    # create a list of all the factors of the input number
    factorsList = []

    # check for factors of the input number
    for i in range(1, math.floor(inputNumber / 2) + 1):
        # add all factors to the factors list
        if inputNumber % i == 0:
            factorsList.append(i)

    # reverse the factors list so it is decreasing order
    # the first prime factor is the largest prime factor
    factorsList.reverse()

    # https://tacomacc.instructure.com/courses/1931063/pages/prime-number-test?module_item_id=41167387
    for value in factorsList:
        isPrime = True
        # find the square root and round down
        valueRoundedSquareRoot = math.floor(math.sqrt(value))

        #start at 2 since every number % 1 == 0
        for i in range(2, valueRoundedSquareRoot + 1):
            if value % i == 0:
                #skip to next value at this point
                isPrime = False

        #first value to be prime is largest prime factor
        if isPrime == True:
            return value

    # blanket return
    return 1
