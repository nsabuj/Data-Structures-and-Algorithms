import sys

n = int(sys.stdin.readline())                                # for size
arr = sys.stdin.readline().split()  # to input n elements

seen = set()

count=0

for i in arr:
    if i not in seen:
        if(arr.count(i)>1):
            count=count+int(arr.count(i)/2)
        seen.add(i)
print(count)    

