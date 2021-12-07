# runtime of sumOfMultiplesBelowNumber(1000, 3, 5) is 0.494s

# takes a number N to search for range(1, N)
# takes variable amount of arguments to test (i % arg == 0)
# sums all multiples of the arguments below the number N
def sumOfMultiplesBelowNumber(N, *args):
    sum = 0

    # test for range (1, N)
    for i in range(N):
        # test all passed arguments
        for arg in args:
            # if i is a multiple of any passed argument
            if i % arg == 0:
                # add i to sum and skip to i + 1
                sum += i
                break

    return sum
