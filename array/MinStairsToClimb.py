def minCostClimbingStairs(cost):
       
        n=len(cost)
        if(n == 0):
                return 0
        if(n == 1):
            return cost[0]        
        
        min_steps=n*[0]
        for i in range(n):
            
            if i<2:
                min_steps[i]=cost[i]
            else:    
                min_steps[i]=cost[i]+ min(min_steps[i-1],min_steps[i-2])
            
        return min(min_steps[n-1],min_steps[n-2])
        
     
     
print(minCostClimbingStairs([10, 15, 20]))