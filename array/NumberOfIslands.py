from collections import deque
def numIslands( grid):
        directions=[[-1,0],[0,1],[1,0],[0,-1]]
        number_of_islands=0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if grid[row][col]=="1":
                    
                    number_of_islands+=1
                    grid[row][col]=="0"
                    queue=deque()

                    queue.append([row,col])
                    print(grid)
                    while len(queue)>0:
                        temp=queue.popleft()

                        current_row=temp[0]
                        current_col=temp[1]
                        for k in range(len(directions)):
                            
                            i=directions[k][0]
                            j=directions[k][1]
                            next_row=current_row+i
                            next_col=current_col+j
                            
                            if next_row<0 or next_row>=len(grid) or next_col<0 or next_col>=len(grid[0]):
                                continue
                            if grid[next_row][next_col]=="1":
                                grid[next_row][next_col]="0"
                                queue.append([next_row,next_col])
                                
        return number_of_islands 


matrix=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(numIslands(matrix))
