# Thanh Nguyen
# CS325 - Fall 2018
# Assignment 5

# -------------------------------------------------------------------------------------------------------------------

# Vertex class to store wrestlers, their side, and their rivals


class Vertex:
    def __init__(ver, val):
        ver.val = val
        ver.adj = []
        ver.side = "Neutral"

# -------------------------------------------------------------------------------------------------------------------


# Read and get filename from command line
import sys
filename = sys.argv[1]

# Create flag variable to decide which output to use at the end
flag = "Possible"

# Create array to hold vertices
adj_list = []

# Open file
fileIn = open(filename, "r")
#fileIn = open("wrestler1.txt", "r")

# Read through the file
for line in fileIn:

    # Get the number of wrestlers aka vertices
    numVer = int(line)

    # increment through the wrestlers and create vertices objects for each
    for x in range(numVer):
        line = next(fileIn)
        ver1 = Vertex(line)
        adj_list.append(ver1)

    # increment the file iterator
    line = next(fileIn)

    # Get the number of rivalries aka edges
    numEdge = int(line)

    # Using the relationships provided, set the vertices' neighbors
    for y in range(numEdge):
        line = next(fileIn)
        arr = line.split(' ')
        z = 0
        for z in range(len(adj_list)):
            if(adj_list[z].val.strip() == arr[0]):
                adj_list[z].adj.append(arr[1].strip())
            if(adj_list[z].val.strip() == arr[1].strip()):
                adj_list[z].adj.append(arr[0].strip())

# Close file
fileIn.close()

# --------------------------------------------------------------------------------------

# Queue for BFS
Q = []

# Array for Babyfaces
Babyfaces = []

# Array for Heels
Heels = []

# Go through all vertices
for a in range(len(adj_list)):

    # If a vertex hasn't been discovered
    if(adj_list[a].side == "Neutral"):
        adj_list[a].side = "Babyface"
        Babyfaces.append(adj_list[a].val.strip())

        # Do BFS

        # Add the vertex to the queue
        Q.append(adj_list[a])

        while(Q != []):

            # Get the current vertex
            curVer = Q.pop()

            # Get the current vertex's side
            curSide = curVer.side

            # ----------------------------------------------------------------------------------

            # Get how many neighbors it has
            adjLen = len(curVer.adj)

            # Create an array to get the index of all of the neighbors
            adjIdx = []

            # Get all neighbors using string matching
            for b in range(adjLen):

                # Set found to false to start
                found = False

                # Set the while counter to 0 to start
                ctr = 0

                # While we haven't found the neighbor
                while(found == False):
                    # If the neighbor matches the vertex of master list
                    if(curVer.adj[b].strip() == adj_list[ctr].val.strip()):
                        adjIdx.append(ctr)
                        found = True
                    ctr = ctr + 1

            # --------------------------------------------------------------------------------

            for c in range(adjLen):
                # If the vertex is undiscovered
                if(adj_list[adjIdx[c]].side == "Neutral"):
                    # If the parent is a Babyface, assign the current child as a Heel and insert it into the BFS queue
                    if(curSide == "Babyface"):
                        adj_list[adjIdx[c]].side = "Heel"
                        Heels.append(adj_list[adjIdx[c]].val.strip())
                        Q.insert(0, adj_list[adjIdx[c]])
                    # If the parent is a Heel, assign the current child as a Babyface and insert it into the BFS queue
                    else:
                        adj_list[adjIdx[c]].side = "Babyface"
                        Babyfaces.append(adj_list[adjIdx[c]].val.strip())
                        Q.insert(0, adj_list[adjIdx[c]])
                # Else the current wrestler has already been discovered and has a side
                else:
                    # If there is a rivalry between same faction, break out of main loop and deem impossible
                    if(curSide == adj_list[adjIdx[c]].side):
                        c = adjLen
                        Q = []
                        a = len(adj_list)
                        flag = "Impossible"

            # -------------------------------------------------------------------------------

# If graph is impossible, specify as such
if(flag == "Impossible"):
    print("Impossible")

# Else, the graph is possible. Specify the names of the Babyfaces and Heels
else:
    print("Yes possible")
    print("Babyfaces:", end=" ")
    for d in range(len(Babyfaces)):
        print(Babyfaces[d], end=" ")
    print()
    print("Heels:", end=" ")
    for e in range(len(Heels)):
        print(Heels[e], end=" ")
    print()
