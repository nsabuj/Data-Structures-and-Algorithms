#codes start here
def selectionSort(arr):
    for i in range(0,len(arr)-1):   #loop through 0 to last index i the array
        min_value=i
        for j in range(i+1,len(arr)):       #loop through unsorted part of the array 
            if(arr[j]<arr[min_value]):      #Find any element less than the last element in the sorted list
                min_value=j
        if min_value!=i:
            arr[i],arr[min_value]=arr[min_value],arr[i]   # swap element

    return arr   #return



print(selectionSort([78,12,10,56,12,19]))                    