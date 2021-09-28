def multipleOfNumber(number):
    i=0
    sum=0
    while i<number:
    
        if i%3==0 or i%5==0:
                
            sum+=i
        i=i+1
    return sum        



print(multipleOfNumber(1000))