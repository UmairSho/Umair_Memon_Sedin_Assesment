"""
Safe Route Navigator
Note: There is a slight change, instead of three directions (F, R, L), This solution 
deals with the grid as a matrix of MxN and instead follow the directions: 
    UP,LEFT,RIGHT,DOWN
"""

from collections import deque
import math

# Below lists details all 4 possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
string = ["U","L","R","D"]

# Function to check if it is possible to go to position (row, col)
# from current position. The function returns false if row, col
# is not a valid position or has value 0 or it is already visited
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
           and mat[row][col] == 1 and not visited[row][col]


# Find Shortest Possible Route in a matrix mat from source 
#and prints the directions but not the shortest path
# cell (i, j) to destination cell (x, y)
def BFS(mat, i, j, x, y):

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()

    # mark source cell as visited and enqueue the source node
    visited[i][j] = True

    # (i, j, dist) represents matrix cell coordinates and its
    # minimum distance from the source
    q.append((i, j, 0))

    # stores length of longest path from source to destination
    min_dist = float('inf')

    #  run till queue is empty
    while q:

        # pop front node from queue and process it
        (i, j, dist) = q.popleft()

        # (i, j) represents current cell and dist stores its
        # minimum distance from the source

        # if destination is found, update min_dist and stop
        if i == x and j == y:
            min_dist = dist
            break
		

        # check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
                print (string[k]+"", end = '')
                break

                
    if min_dist == float('inf'):
        print("\nDestination can't be reached")

#This function is to convert decimal house numbers to the specific coordinates
#in terms of i and j pointing a specific cell in the grid

def convert(housenumber,M,N):
    i = math.ceil(housenumber/N) - 1
    j = housenumber-(N*(i)) -1
    return (i,j)
  

if __name__ == '__main__':


    
    # take inputs
    print("Enter the number of rows and columns in the grid seperated by space:")
    sizeofgrid = [ int(x) for x in input().split()] 
    print("size of grid:", sizeofgrid) 
    M = sizeofgrid[0]
    N = sizeofgrid[1]
    mat = [ [ 1 for i in range(M) ] for j in range(N) ]
    
    print("Enter Houses Quarantined,seperated by spaces:")
    housesquarantined = [ int(x) for x in input().split()] 
    print("houses quarantined:", housesquarantined)
    print("Enter Destination House number")
    Destinationhouse = int(input())
    print("Destination house number: ", Destinationhouse)
    
    i,j = convert(Destinationhouse,M,N)
    
    for house in housesquarantined:
        quarantine_index_i,quarantine_index_j = convert(house, M, N)
        mat[quarantine_index_i][quarantine_index_j] = 0
    BFS(mat, 0, 0, i, j)
