from factors import *

# runtime for largestPalindromeProduct(3) is 0.098s

# find the largest palindrome made from the product of two N digit numbers
def largestPalindromeProduct(N):

    # find largest number given N digits
    # largest 1 digit number is 9, largest 2 digit number is 99
    largestNDigitNumber = ""
    for i in range(N):
        largestNDigitNumber = largestNDigitNumber + "9"
    largestNDigitNumber = int(largestNDigitNumber)

    # find the largest number of the product of two N digit numbers
    squaredLargestNDigitNumber = largestNDigitNumber ** 2

    # search for palindromes in decreasing order
    for i in range(squaredLargestNDigitNumber, 0, -1):
        # if number is a palindrome
        if str(i) == str(i)[::-1]:
            # get all factor pairs of the number
            factorPairList = findFactorPairs(i)

            # return factor pair exists that meets requirements
            for factorPair in factorPairList:
                if factorPair[0] <= largestNDigitNumber and factorPair[1] <= largestNDigitNumber:
                    return i

    # blanket return
    return 2
