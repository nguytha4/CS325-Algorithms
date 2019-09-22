# stoogesort function: A is the array, n is the number of elements in the array
def stoogesort(A, i, j):

    # number of elements in array
    n = j - i + 1

    # if only one element in the array, already sorted
    if(i >= j):
        return

    # if first element larger than last element, swap
    if(A[i] > A[j]):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    # if there are more than 2 elements in the array
    if(n > 2):
        # Find the 1/3rd point of the array
        t = n / 3
        tInt = int(t)
        # Sort the first 2/3rds of the array
        stoogesort(A, i, (j - tInt))
        # Sort the last 2/3rds of the array
        stoogesort(A, i + tInt, (j))
        # Sort the first 2/3rds of the array
        stoogesort(A, i, (j - tInt))

# ============================================================================


# Open file
fileIn = open("data.txt", "r")
fileOut = open("stooge.out", "w+")

# Read a line in the file
for line in fileIn:
    arr = line.split(' ')

    # Get the length of the array as an int
    length_str = arr[0]
    length = int(length_str)

    # Make a new array to hold the values of the read array as ints
    arr2 = [0] * length

    # Put contents of string array into new array; remember: first value of read array is the length so we don't copy that
    i = 0
    while i < length:
        arr2[i] = int(arr[i + 1])
        i += 1

    # Sort the array
    stoogesort(arr2, 0, length - 1)

    # Output the array into a file
    for nums in arr2:
        fileOut.write(str(nums))
        fileOut.write(" ")
    fileOut.write("\n")

# Close the file
fileIn.close()
fileOut.close()
