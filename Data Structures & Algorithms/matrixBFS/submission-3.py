from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #Shortest Path and I thought of a BFS because it would run more efficiently than DFS
        #DFS is like 4^n vs BFS is the size of the grid O(n)
        #Input is a grid 0s are traversable 1 is blocked
        #We want to go from top left to bottom right 
        #BFS
        #visualize the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        #a queue to insert every traversable level
        queue = deque()
        #need to track every position that we have visited
        #avoid infinite loop
        visit = set()

        #we should start at the top left
        visit.add((0,0))

        queue.append((0,0))

        #return the length of the shortest path 
        length = 0
        #go through the queue while it's not empty
        while queue:
            #go through the items in the queue
            for i in range(len(queue)):
                #pop the items out of the queue
                row, col = queue.popleft()

                #Check if we have reached the bottom right corner
                if row == ROWS - 1 and col == COLS - 1:
                    return length


                #If we haven't found the path we need to traverse the grid
                directions = [
                    [1,0],
                    [-1,0],
                    [0,1],
                    [0,-1]
                ]

                #go through the directions
                for dr, dc in directions:
                    #we have a bunch of base cases
                    #if we aren't in bounds
                    #or the position plus movement is out of bounds
                    #if we hit a blocked position
                    #if we already visited the position
                    if ( min(row + dr,col + dc) < 0 or row + dr == ROWS or 
                    col + dc == COLS or grid[row + dr][col + dc] == 1 or
                    (row + dr, col + dc) in visit):
                        #check the next position
                        continue
                    
                    queue.append((row + dr, col + dc))
                    visit.add((row + dr, col + dc))
            length += 1 

        return -1


                
