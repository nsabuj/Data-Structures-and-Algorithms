def isPrime(num):
    
    nums_to_check = range(2, int(num**.5) + 1)
    for i in nums_to_check:
        if num%i==0:
            return False
    return True        


def NthPrimeNumber(N):
    i=2
    nth_prime=1
    while nth_prime<N:
        i+=1
        if isPrime(i):
            nth_prime+=1
         
    return i       


print(NthPrimeNumber(10001))