

from itertools import permutations

def Permutation(str,ans,rtn):
    if len(str)<1:
        
        rtn.append(ans)
        
        return
  
    for i in range(len(str)):
        result=str[i]
        rem=str[:i]+str[i+1:]
        Permutation(rem,ans+result,rtn)

    return rtn   



data = list('ABC')
print(Permutation(data,'',[]))
