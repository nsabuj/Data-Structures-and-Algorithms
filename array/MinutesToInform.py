def numOfMinutes( n, headID, manager, informTime):
    
   
    adj_list=[[] for i in range(n)]
    for key,employee in enumerate(manager):
        if key==headID:
            continue
        
        
        adj_list[employee].append(key)
        
    return DFS(headID,adj_list,informTime)



def DFS(current_id,list,minutes):
    if len(list[current_id])<1:
        return 0
    max_minutes=0
    employees=list[current_id]
    for j in employees:
        
        max_minutes=max(max_minutes,DFS(j,list,minutes))
    return max_minutes+minutes[current_id]    


print(numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))