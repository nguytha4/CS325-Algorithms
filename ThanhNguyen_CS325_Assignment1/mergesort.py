# merge sort function; A is the array
def mergeSort(A):

    if len(A) > 1:
        mid = len(A) // 2
        lower = A[:mid]
        upper = A[mid:]

        # recursion
        mergeSort(lower)
        mergeSort(upper)

        i = 0
        j = 0
        k = 0

        while i < len(lower) and j < len(upper):
            if lower[i] < upper[j]:
                A[k] = lower[i]
                i = i + 1
            else:
                A[k] = upper[j]
                j = j + 1
            k = k + 1

        while i < len(lower):
            A[k] = lower[i]
            i = i + 1
            k = k + 1

        while j < len(upper):
            A[k] = upper[j]
            j = j + 1
            k = k + 1

# ============================================================================


# Open file
fileIn = open("data.txt", "r")
fileOut = open("merge.out", "w+")

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
    mergeSort(arr2)

    # Output the array into a file
    for nums in arr2:
        fileOut.write(str(nums))
        fileOut.write(" ")
    fileOut.write("\n")

# Close the file
fileIn.close()
fileOut.close()
