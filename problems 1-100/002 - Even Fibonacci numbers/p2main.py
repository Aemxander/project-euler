# runtime of sumEvenFibonacciNumbersBelow(4000000) is 0.602s

# sum all even fibonacci numbers below N
def sumEvenFibonacciNumbersBelow(N):
    # first two numbers of fibonacci sequence
    fibonacciSequence = [1, 2]
    # index of last item in list
    currentIndex = 1

    # checks if the next fibonacci number is less than inputNumber
    while (fibonacciSequence[currentIndex-1] + fibonacciSequence[currentIndex]) < N:
        # calculate new fibonacci number
        newTerm = fibonacciSequence[currentIndex-1] + fibonacciSequence[currentIndex]
        # add fibonacci number to sequence
        fibonacciSequence.append(newTerm)

        # increment index
        currentIndex += 1

    # sum for even fibonacci numbers
    sum = 0

    # check all fibonacci numbers
    for value in fibonacciSequence:
        # add fibonacci number to sum if even
        if value % 2 == 0:
            sum += value

    # return sum of even fibonacci numbers below N
    return sum
