def mergeSort(arr):
    if(len(arr)>1):

        #Finding the middle index of the array
        mid=len(arr)//2  
        #coping all the elements of left side of the array to a temporary array L
        L= arr[:mid] 
        
        # coping all the items starting from middle to all  
        # the way to the last element to a temporary array R       
        R= arr[mid:] 
    
        #Recursively calling mergeSort fuction with the splitted array
        mergeSort(L)
        mergeSort(R)  
        
        i=j=k=0
        # Run the loop through both portion of array
        # Check if item from left array is smaller or not than the next item
        #from right array, thus store them in acsending order 
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
                
            else:
                arr[k]=R[j]
                j+=1
            k+=1     

        # Now loop through remaining item from both
        # arrays
        while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1

        while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1

    return arr

    arr=[10,4,5,12,59,15,61,10]
    print(mergeSort(arr))

# Time complexity is n*log(n)