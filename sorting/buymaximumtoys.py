def maximumToys(prices, k):
    # Write your code here
 
    items=0
    sum=0
    prices.sort()
   
    for i in prices:
        
        if k-sum>=i:
            
            items+=1
            sum=sum+i
            
            
    return items
if __name__ == '__main__':
   



    result = maximumToys([6,3,4,1,7], 11)

    print(result)
