from findFactorPairs import *

# runtime for largestPalindromeProduct(3) is 0.098s

# find the largest palindrome made from the product of two X digit numbers
def largestPalindromeProduct(X):

    # find largest number given X digits
    # largest 1 digit number is 9, largest 2 digit number is 99
    largestXDigitNumber = ""
    for i in range(X):
        largestXDigitNumber = largestXDigitNumber + "9"
    largestXDigitNumber = int(largestXDigitNumber)

    # find the largest number of the product of two X digit numbers
    squaredLargestXDigitNumber = largestXDigitNumber ** 2

    # search for palindromes in decreasing order
    for i in range(squaredLargestXDigitNumber, 0, -1):
        # if number is a palindrome
        if str(i) == str(i)[::-1]:
            # get all factor pairs of the number
            factorPairList = findFactorPairs(i)

            # return factor pair exists that meets requirements
            for factorPair in factorPairList:
                if factorPair[0] <= largestXDigitNumber and factorPair[1] <= largestXDigitNumber:
                    return i

    # blanket return
    return 2
