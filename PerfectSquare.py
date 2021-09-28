import math
def numSquares( n: int) -> int:
        minnumber=[0,1,2,3]  
        
        for i in range(4,n+1):
            
            minnumber.append(i)
            
            for j in range(1,int(math.ceil(math.sqrt(i)))+1):
                
                temp=j*j
                if temp>i:
                    break
                else: 
                    minnumber[i]= min(minnumber[i],1 + minnumber[i-temp])


        return minnumber[n]    

                    
        
        

      

print(numSquares(45))        