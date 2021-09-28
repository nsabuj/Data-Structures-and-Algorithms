def isPrime(num):
    #Brute force method
    nums_to_check = range(2, int(num**.5) + 1)
    for i in nums_to_check:
        if num%i==0:
            return False
    return True   

def SumOfPrime(N):
    sum=0
    for i in range(2,N):
        if isPrime(i):
            sum+=i
    return sum

def SumOfPrime2(N):
   
    #Efficient way
    # create a set excluding even numbers
    numbers = set(range(3, N + 1, 2)) 
   
    for number in range(3, int(N ** 0.5) + 1):
        if number not in numbers:
            #number must have been removed because it has a prime factor
            continue

        num = number
        while num < N:
            num += number
            if num in numbers:
                # Remove multiples of prime found
                numbers.remove(num)
    return 2 + sum(numbers)
print(SumOfPrime2(2000000))
#print(SumOfPrime(2000000))    
