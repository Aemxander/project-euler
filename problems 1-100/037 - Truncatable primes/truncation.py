from removeDigits import *

# check if a number is left truncatable and right truncatable
# pass a number and a list of all primes below/equal to the number
def checkIfLeftRightTruncatablePrime(number, primes):
    # return True if left and right truncatable
    if checkIfRightTruncatablePrime(number, primes) == True and checkIfLeftTruncatablePrime(number, primes) == True:
        return True
    # return False if not left and right truncatable
    else:
        return False

# check if a number is right truncatable
# pass a number and a list of all primes below/equal to the number
def checkIfRightTruncatablePrime(number, primes):
    # infinite loop until it hits a return statement
    while True:

        # if more than 1 digit
        if number >= 10:
            # remove last digit
            number = removeOneDigitFromRight(number)

            # return False if new number isn't in prime list
            if number not in primes:
                return False

        # if 1 digit
        if number < 10:
            # return False if number isn't in prime list
            if number not in primes:
                return False
            # return True if entire number is right truncatable
            else:
                return True

# check if a number is right truncatable
# pass a number and a list of all primes below/equal to the number
def checkIfLeftTruncatablePrime(number, primes):
    # infinite loop until it hits a return statement
    while True:

        # if more than 1 digit
        if number >= 10:
            # remove first digit
            number = removeOneDigitFromLeft(number)

            # return False if new number isn't in prime list
            if number not in primes:
                return False

        # if 1 digit
        if number < 10:
            # return False if number isn't in prime list
            if number not in primes:
                return False
            # return True if entire number is left truncatable
            else:
                return True
