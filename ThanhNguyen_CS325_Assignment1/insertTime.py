import random
import time

# ===========================================================================

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

# function to generate an array of random values; lower = lowest value an int could have, upper = greatest value an int could have, num = number of elements


def randomArr(lower, upper, num):
    arr = []

    for j in range(num):
        arr.append(random.randint(lower, upper))

    return arr

# ============================================================================


# Test case #1, n = 5000
print("Test #1:")

# Generate random array
start = 0
end = 10000
num = 5000
arr1 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr1, 5000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #2, n = 10000
print("Test #2:")

# Generate random array
start = 0
end = 10000
num = 10000
arr2 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr2, 10000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #3, n = 15000
print("Test #3:")

# Generate random array
start = 0
end = 10000
num = 15000
arr3 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr3, 15000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #4, n = 20000
print("Test #4:")

# Generate random array
start = 0
end = 10000
num = 20000
arr4 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr4, 20000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #5, n = 30000
print("Test #5:")

# Generate random array
start = 0
end = 10000
num = 30000
arr5 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr5, 30000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #6, n = 40000
print("Test #6:")

# Generate random array
start = 0
end = 10000
num = 40000
arr6 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr6, 40000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds\n")

# ============================================================================


# Test case #7, n = 50000
print("Test #7:")

# Generate random array
start = 0
end = 10000
num = 50000
arr7 = randomArr(start, end, num)

# Sort the array and log the time
start_time = time.time()
insertionSort(arr7, 50000)
took_time = time.time() - start_time

# Print the results of the test
print("Value of n:", num, "| Time elapsed:", took_time, "seconds")
