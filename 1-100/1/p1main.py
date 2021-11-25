#takes an input number to search for range(1, inputNumber)
#takes variable amount of arguments to test (i % arg == 0)
def SumOfMultiplesBelowNumber(inputNumber, *args):
    sum = 0

    #test for range (1, inputNumber)
    for i in range(inputNumber):
        #test all passed arguments
        for arg in args:
            #if i is a multiple of any passed argument
            if i % arg == 0:
                #add i to sum and skip to i + 1
                sum += i
                break

    return sum