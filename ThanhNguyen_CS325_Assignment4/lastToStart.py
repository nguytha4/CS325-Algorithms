# Thanh Nguyen
# CS325 - Fall 2018
# Assignment 4

# -------------------------------------------------------------------------------------------------

# find the greatest number of activies that can be done
# choosing based on earliest start time


def greedyActSel(acts):

    # n is the number of activites
    n = len(acts)

    # A will hold the optimal set
    A = []

    # i will serve as the placeholder for last selected activity
    i = 0

    # add the activity with the latest starting time
    A.append(acts[0].n)

    # Starting with the second element, find the next activity a compatible finish time
    for m in range(1, n):
        if(acts[m].f <= acts[i].s):
            A.insert(0, acts[m].n)
            i = m

    # Print the results
    print("Number of activities selected =", len(A))
    print("Activities:", end=" ")
    for x in range(len(A)):
        print(A[x], end=" ")

# -------------------------------------------------------------------------------------------------

# Create a class to represent an activity with a number, start time, and finish time


class Activity:
    def __init__(act, n, s, f):
        act.n = n
        act.s = s
        act.f = f

# -------------------------------------------------------------------------------------------------

# Key to use for sorting. Tell sorting to reference start time


def takeSecond(elem):
    return elem.s

# -------------------------------------------------------------------------------------------------


# Open file
fileIn = open("act.txt", "r")

# Activity counter
setCtr = 1

# Get the number of lines for each activity
for line in fileIn:

    # get the number of activities
    numAct = int(line)

    # Arrays to hold the activities
    arr2 = []

    # increment through the activities and get their start/finish times
    for x in range(numAct):
        line = next(fileIn)
        arr = line.split(' ')
        n = int(arr[0])
        s = int(arr[1])
        f = int(arr[2])
        act1 = Activity(n, s, f)
        arr2.append(act1)

    arr2.sort(key=takeSecond, reverse=True)

    print("Set", setCtr)

    greedyActSel(arr2)

    # Increment the number of test cases
    setCtr += 1

    # Print newline in between sets
    print("\n")

# Close the file
fileIn.close()
