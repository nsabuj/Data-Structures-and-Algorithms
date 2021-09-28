def EvenFibonacciNumber(limit):
    i=2
    sum_of_even=0
    a=0
    fibo=[0,1] #initializing for n=0 and n=1
    while a<=limit:
        
        a=fibo[i-1]+fibo[i-2]
        if a<limit:
            fibo.append(a)
            
            if a%2==0: 
                sum_of_even=sum_of_even+a
            
        else:
            break 
        
        i=i+1       
      
    return sum_of_even

def EvenFibonacciNumber2(limit):  #optimized way
        a, b = 1, 1
        total = 0
        while a <= limit:
            if a % 2 == 0:
                total += a
            a, b = b, a+b  # the real formula for Fibonacci sequence
        return total

print(EvenFibonacciNumber2(4000000))