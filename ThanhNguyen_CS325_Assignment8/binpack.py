# Thanh Nguyen
# CS325 - Fall 2018
# Assignment 8

# -------------------------------------------------------------------------------------------------------------------

# ========================================================================================================

# First-Fit algorithm


def firstFit(w, n, c):

    bins = 0            # Initialize the starting number of bins to 0

    bins_space = []     # Create an array to hold how much space a bin has left

    # Outer loop to iterate through items
    for i in range(n):
        # Inner loop to iterate through bins
        j = 0
        while (j < bins):
            # If bin we're looking at has space, add item to bin and update space it has
            if(bins_space[j] >= w[i]):
                bins_space[j] = bins_space[j] - w[i]
                break
            j = j + 1
        # If no bins have space, add a new bin
        if (j == bins):
            leftover = c - w[i]
            bins_space.append(leftover)
            bins = bins + 1
    return bins

# ========================================================================================================

# First-Fit-Decreasing algorithm


def firstFitDec(w, n, c):

    # sort items in decreasing order
    w.sort(reverse=True)
    return firstFit(w, n, c)

# ========================================================================================================


def bestFit(w, n, c):

    bins = 0            # Initialize the starting number of bins to 0

    bins_space = []     # Create an array to hold how much space a bin has left

    bi = 0              # index of bin with min space after adding an item

    # Outer loop to iterate through items
    for i in range(n):
        j = 0
        minVal = c + 1      # value of bin with min space after adding an item
        # Inner loop to iterate through bins
        while (j < bins):
            # If item fits in bin and if item fits in bins with minimal val
            if(bins_space[j] >= w[i] and bins_space[j] - w[i] < minVal):
                bi = j                          # Get the index of bin with best min val
                minVal = bins_space[j] - w[i]   # Set the new min val
            j = j + 1
        # If no bin can fit item, add a new bin
        if (minVal == c + 1):
            leftover = c - w[i]
            bins_space.append(leftover)
            bins = bins + 1
        # Else, add the item to the bin with best min val
        else:
            bins_space[bi] = bins_space[bi] - w[i]
    return bins

# ========================================================================================================


# Open file
fileIn = open("bin.txt", "r")

# Get the number of test cases
testCases = int(fileIn.readline())

# Test case counter
testCaseCtr = 0

# Variable to hold the number of items and capacity per test case
n = 0
c = 0

# Get the number of lines for each test case
for line in fileIn:

    # Arrays to hold the weights of items
    w = []

    # Increment the number of test cases
    testCaseCtr += 1

    # get the capacity of the bins
    c = int(line)

    # increment the file iterator
    line = next(fileIn)

    # get the number of items to pack
    n = int(line)

    # increment the file iterator
    line = next(fileIn)

    # split the line of weights
    arr = line.split(' ')

    # increment through the items in the file and get their weights
    for x in range(n):
        w.append(int(arr[x]))

    # ---------------------------------------------------------------------------------

    # call the First Fit function
    ff = firstFit(w, n, c)

    # call the First-Fit-Decreasing function
    w2 = []                     # Need to create a new array of weights for sorted items
    for a in range(len(w)):
        w2.append(w[a])

    ffd = firstFitDec(w2, n, c)

    # call the Best Fit function
    bf = bestFit(w, n, c)

    # Print the results
    print("Test Case", testCaseCtr, end="")
    print(" First Fit:", ff, end="")
    print(", First Fit Decreasing:", ffd, end="")
    print(", Best Fit:", bf)

# Close the files
fileIn.close()
