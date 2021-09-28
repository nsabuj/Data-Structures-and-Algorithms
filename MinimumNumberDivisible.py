
import math

def GCD(x,y):   # GCD returns greatest common divisible value
   while(y):
       x, y = y, x % y
  
   return x


def MinimumNumberDivisible(n):
    
    ans = 1
    for i in range(1, n + 1):
        
 #       ans = int((ans * i)/math.gcd(ans, i))
        ans = int((ans * i)/GCD(ans, i))
                
    return ans



print(MinimumNumberDivisible(20))    
#time complexity O(n)
#space complexity O(1)