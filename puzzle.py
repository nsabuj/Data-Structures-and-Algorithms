
def jumpingOnClouds(c):
    # Write your code here
    count=0
    i=0
    while i<len(c):
        if c[i]==0:
            count+=1
            if i+2<len(c) and c[i+2]==0 :
                i+=2
            else:      # given, this is always possible to travel, so no need to check validity here
                i+=1     
    return count
if __name__ == '__main__':
   c=[0, 0, 0, 0, 1, 0]

   result = jumpingOnClouds(c)
   print(result)
