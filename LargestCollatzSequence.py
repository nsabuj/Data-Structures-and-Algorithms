
from typing import Sequence


def LargestCollatzSequence(number):
   
    #dp=[-1]*number
    starting_number=0
    Sequencelength=0
    dp=[0,1]
    for j in range(2,number):
        dp.append(j)
        count=0
        i=j
        while i != 1 and i >= j:
            count+=1
            if i%2==0:
                i=int(i/2)
            else:
                i=3*i+1    
                
        dp[j]=count+dp[i]  
        if dp[j] > Sequencelength: 
                Sequencelength = dp[j]
                starting_number = j
                

    return starting_number


print(LargestCollatzSequence(1000000))