
def Heapyfy(arr,i,n):
  
        l=i*2+1
        r=i*2+2
        largest=i
        if(l<n and arr[l]>arr[i]):
            largest=l
        if(r<n and arr[r]>arr[largest]):
            largest=r
        if(i!=largest):
            arr[i],arr[largest]=arr[largest],arr[i]
            Heapyfy(arr,largest,n)



def Heap(arr):
    n=len(arr)  # Length of array
    #start loop from the root to the last element
    for i in range(n//2-1,-1,-1):
        
        Heapyfy(arr,i,n)
 
    for i in range(n-1, 0, -1):
        
        arr[i], arr[0] = arr[0], arr[i]   # swap

        Heapyfy(arr, 0, i)
   


def DeleteHeap(arr):
    n=len(arr)
    del_item=arr.remove(12)
    for i in range(n-2, 0, -1):
        
        arr[i], arr[0] = arr[0], arr[i]   # swap

        Heapyfy(arr, 0, i)
    return del_item

arr=[9,10,12,5,5,4,56]
Heap(arr)
print(arr)



