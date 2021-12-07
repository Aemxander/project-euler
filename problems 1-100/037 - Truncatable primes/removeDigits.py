import math

# remove the last digit from a number
def removeOneDigitFromRight(number):
    # removes last digit by dividing by 10 and rounding down
    return math.floor(number / 10)

#mcswaggy code made from biscuit scratch
#condense into one line if you want blindness
# remove the first digit from a number
def removeOneDigitFromLeft(number):
    # calculates 1 less than amount digits in number
    oneLessDigits = math.floor(math.log10(number))

    # get first digit of number
    firstDigit = math.floor(number / (10 ** oneLessDigits))

    # remove first digit of number
    number -= firstDigit * (10 ** oneLessDigits)

    # return number with first digit removed
    return number
