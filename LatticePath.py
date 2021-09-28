def LatticePath(grid):
    routes=[[0 for i in range(grid+1)] for i in range(grid+1)]
    queue=[(grid,grid)]
    routes[grid][grid]=1
    while queue:
        
        current=queue.pop(0)
        
        if current[0]-1>=0:
            if (current[0]-1,current[1]) not in queue:
                queue.append((current[0]-1,current[1]))
            routes[current[0]-1][current[1]]+=routes[current[0]][current[1]]

        if current[1]-1>=0:
            if (current[0],current[1]-1) not in queue:
                queue.append((current[0],current[1]-1))
            routes[current[0]][current[1]-1]+=routes[current[0]][current[1]]            

    return routes[0][0]


print(LatticePath(20))    