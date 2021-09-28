def SumOfNaturulNumber(n):
   sum=0
   sum_of_squre=0 
   for i in range(1,n+1):
       sum+=i
       sum_of_squre+=i*i
   return (sum*sum)-sum_of_squre
    



print(SumOfNaturulNumber(100))    