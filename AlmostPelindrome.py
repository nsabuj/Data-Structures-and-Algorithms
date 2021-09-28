

def IsPelindrome(s,left,right):
    while left<right:
        if s[left]!=s[right]:
           return False

        left+=1
        right-=1
    return True       


def AlmostPelindrome(s):
    if len(s)<3:
        return True
    
   
    left=0
    right=len(s)-1
   
    while left<right:

        if s[left] is not s[right]:
  
           return IsPelindrome(s,left+1,right) or IsPelindrome(s,left,right-1)

        left+=1
        right-=1    


    return True



print(AlmostPelindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))    