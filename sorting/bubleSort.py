def countSwaps(a):
    # Write your code here
    swaps=0
    n=len(a)
    for i in range(n-1):
       for j in range(n-1):
           if(a[j]>a[j+1]):  #checking if the current element is larger than the next element
               swaps+=1  #counts swaps
               a[j],a[j+1]=a[j+1],a[j] #swapping 
    print("Array is sorted in "+str(swaps)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))
if __name__ == '__main__':

    countSwaps([1,3,9,6,7])