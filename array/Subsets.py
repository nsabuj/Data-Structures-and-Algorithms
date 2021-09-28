from functools import reduce
import operator
def SubSets(arr):
    if arr==[]:
        return [[]]

    x=SubSets(arr[1:])
    return x+[[arr[0]]+ i for i in x] 



def FindSubsetsConditionally(arr):
#    return [subset for subset in SubSets(arr) if len(subset)>2]   # if required output is min 3 elem of subsets
     return [subset for subset in SubSets(arr) if reduce(operator.mul, subset,1)<90 and len(subset)>0]
   
arr=[2,5,6,7]

print(FindSubsetsConditionally(arr))