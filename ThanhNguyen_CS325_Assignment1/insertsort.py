# insertion sort function; A is the array, n is the length of the array
def insertionSort(A, n):
    j = 1
    while j < n:
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        j += 1

# ============================================================================


# Open file
fileIn = open("data.txt", "r")
fileOut = open("insert.out", "w+")

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
    insertionSort(arr2, length)

    # Output the array into a file
    for nums in arr2:
        fileOut.write(str(nums))
        fileOut.write(" ")
    fileOut.write("\n")

# Close the file
fileIn.close()
fileOut.close()
