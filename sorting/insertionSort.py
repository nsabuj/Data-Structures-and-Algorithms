def insertionSort(arr):
    for i in range(0,len(arr)-1):
        
        while arr[i-1]>arr[i] and i>0:
            print(i)
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i-=1

    return arr   




print(insertionSort([3,4,7,12,2,7,9,34]))