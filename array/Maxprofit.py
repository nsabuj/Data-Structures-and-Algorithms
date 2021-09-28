# Python3 implementation of the approach
import math
from collections import defaultdict
# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks
def maxProfit(price, start, end):
 
    # If the stocks can't be bought
    if (end <= start):
        return 0;
 
    # Initialise the profit
    profit = 0;
 
    # The day at which the stock
    # must be bought
    maxProfit=[]
    for i in range(start, end, 1):
 
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
 
            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                 
                # Update the current profit
                curr_profit = price[j] - price[i]+maxProfit(price,start,i-1)+maxProfit(price,j+1,end);
 
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
 
    return profit;
def maxProfit2( price):
    # Prices must be given for at least two days
    n=len(price)
    if (n == 1):
        return
     
    # Traverse through given price array
    i = 0
    max_Profit=defaultdict(list)
    max_days=[]
    while (i < (n - 1)):
      
         
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1
        print(i) 
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
         
        # Store the index of minima
        buy = i
        i += 1
         
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
             
        # Store the index of maxima
        sell = i - 1
        max_Profit[price[sell]-price[buy]]=(buy,sell)
    max_days=sorted(max_Profit.keys()) 
    
    return max_Profit[max(max_days)][0]

def maxProfit3(prices):           # Max profit
        n=len(prices)
        if (n <2):
            return 0
        max_profit=float("-inf")
        min_stock=prices[0]
        
        for i in range(1,n):
            min_stock=min(min_stock,prices[i])
            max_profit=max(max_profit,prices[i]-min_stock)
            
        return max_profit
def TotalProfit(prices):

        profit=0
        left=1
        right=len(prices)
        while left<right:
            if prices[left-1]<prices[left]:
                profit+=prices[left]-prices[left-1]
            left+=1   
        return profit 


def maxProfit4( prices):
        if len(prices)<2:
            return 0
        
        left=1
        right=len(prices)
        profits=[]
        while left<right:
            if prices[left-1]<prices[left]:
                profits.append(prices[left]-prices[left-1])
            left+=1
        print(profits)       
        profits.sort(reverse=True)
        return sum(profits[:2])





# Driver code


if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695];
    price2=[3,2,6,5,0,3]
    n = len(price);
 
    print(maxProfit2(price));
 
# This code is contributed by Rajput-Ji