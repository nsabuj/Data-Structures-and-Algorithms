def quickSort(arr):
    if(len(arr)<=1):
        return arr
    else:

        pivot=arr.pop()
        lower_items=[]
        higher_items=[]
        i=0
        while(i<len(arr)):
            if arr[i]<pivot:
                lower_items.append(arr[i])
            else:
                higher_items.append(arr[i])
            i+=1       
    return quickSort(lower_items)+[pivot]+quickSort(higher_items)                











arr=[56,12,10,6,14,10,14,18,13,16]
print(quickSort(arr))