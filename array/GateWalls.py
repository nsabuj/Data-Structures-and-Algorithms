def wallsAndGates( rooms):
            # write your code here
        wall=-1
        gate=0
        
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col]==gate:
                   dfs(rooms,row,col,0)

        return rooms

def dfs(rooms,row,col,count):
         if row<0 or row>=len(rooms) or col<0 or col>=len(rooms[0]) or count>rooms[row][col] or rooms[row][col]==-1:
            return
         rooms[row][col]=count   
         adjacent_rows=[-1,0,1,0]
         adjacent_cols=[0,1,0,-1]
         for k in range(len(adjacent_rows)):
             next_row=row+adjacent_rows[k]
             next_col=col+adjacent_cols[k]
             dfs(rooms,next_row,next_col,count+1)  
             
matrix=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

print(wallsAndGates(matrix))