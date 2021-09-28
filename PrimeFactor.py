

def isPrime(number):
    i=2
    while i<number-1:
        if number%i==0:
            return False
            
        i+=1    
    return True

def PrimeFactor(value):
    i=2
    if value%2==0:
        value=value/2
        i=3
    factors=[]
    while i<value+1:
    #for i in range(3,value+1,2):
        
        if value%i==0:
            if(isPrime(i)):
                factors.append(i)
                value=value/i
        i+=1
    return max(factors)





print(PrimeFactor(600851475143 ))           

