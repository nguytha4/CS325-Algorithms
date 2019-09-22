# Thanh Nguyen
# CS325 - Fall 2018
# Assignment 3

# ========================================================================================================

# shopCart function to determine what items each family member should buy
# W is the max weight the strongest member of the family can carry
# wt is the weight of the items
# val is the value of the items
# n is the number of items


def shopCart(W, wt, val, n):
    # Initialize two-dimentional array of items and "knapsack" weight
    S = [[0 for x in range(W + 1)] for y in range(n + 1)]

    # initialize 0th column to 0
    for i in range(n + 1):
        S[i][0] = 0

    # initialize 0th row to 0
    for j in range(1, W + 1):
        S[0][j] = 0

    # start filling out the array

    # i = rows = items
    for i in range(1, n + 1):

        # j = columns = "knapsack" weights
        for j in range(1, W + 1):
            # if the current item can fit into the shopping cart
            if(wt[i - 1] <= j):
                # add it into the cart, and the best value it contributes after subtracting its weight
                # compare this to the maximum of the cart if this item was not selected
                S[i][j] = max(val[i - 1] + S[i - 1][j - wt[i - 1]], S[i - 1][j])
            else:
                # else, use the best value at this weight excluding this item (value from the previous item)
                S[i][j] = S[i - 1][j]

    return S

# ========================================================================================================

# calculating the price of the shopping spree
# S is the array of optimal prices
# fam is the family members and the weight they can carry
# n is the number of items
# f is number of family members


def calcPrice(S, fam, n, f):

    total = 0

    # using the array of optimal prices, reference the family member's weight and the last row and append to the total
    for i in range(f):
        total += S[n][fam[i]]

    return total

# ========================================================================================================

# Get the items per person
# S is the array of optimal prices
# weight is the amount the current person can carry
# wt is weight of the items
# n is the number of items


def itemList(S, weight, wt, n):

    # store the recommended items a person should carry
    C = []

    # while we still have items a person might be able to carry
    while(n > 0):
        # if the optimal price of the element above is equal to the current element, move up
        if(S[n - 1][weight] == S[n][weight]):
            n -= 1
        # else, the element is a recommended item. move one row up and subtract the weight of the item
        else:
            C.insert(0, n)
            weight -= wt[n - 1]
            n -= 1

    return C

# ========================================================================================================



# Open file
fileIn = open("shopping.txt", "r")
fileOut = open("shopping.out", "w+")

# Get the number of test cases
testCases = int(fileIn.readline())

# Test case counter
testCaseCtr = 0

# Variable to hold the number of items and family members per test case
numItems = 0
numFam = 0

# Get the number of lines for each test case
for line in fileIn:

    # Arrays to hold the weight, value of items / and family members and weights
    val = []
    wt = []
    fam = []

    # Increment the number of test cases
    testCaseCtr += 1

    # get the number of items
    numItems = int(line)

    # increment through the items in the file
    #       and get the items at the same time
    for x in range(numItems):
        line = next(fileIn)
        arr = line.split(' ')
        val.append(int(arr[0]))
        wt.append(int(arr[1]))

    # increment the file iterator
    line = next(fileIn)

    # get the number of items
    numItems = len(val)

    # get the number of family members
    numFam = int(line)

    # increment through the family members in the file
    for y in range(numFam):
        line = next(fileIn)
        fam.append(int(line))

    # Get the weight of the strongest person in the family
    W = max(fam)

    # call the shopCart function
    arr = shopCart(W, wt, val, numItems)

    # calculate the price for this shopping spree
    numFam = len(fam)
    cost = calcPrice(arr, fam, numItems, numFam)

    # Print out the headers for the test cases onto the output file
    fileOut.write("Test Case ")
    fileOut.write(str(testCaseCtr))
    fileOut.write("\n")

    fileOut.write("Total Price ")
    fileOut.write(str(cost))
    fileOut.write("\n")

    fileOut.write("Member Items:")
    fileOut.write("\n")

    # list out the items that each person bought
    for z in range(numFam):
        fileOut.write(str(z + 1))
        fileOut.write(": ")
        cart = itemList(arr, fam[z], wt, numItems)
        # print out the individual's cart
        for v in range(len(cart)):
            fileOut.write(str(cart[v]))
            fileOut.write(" ")
        fileOut.write("\n")

    fileOut.write("\n")

# Close the files
fileIn.close()
fileOut.close()

# ========================================================================================================
