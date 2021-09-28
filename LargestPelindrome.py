def isPelindrome(num):
    return num == num[::-1]

def BiggestPelindrome(n):
    biggest_pelindrome=0
   
    for i in range(1,n):
        for j in range(1,n):
            multi=i*j
            if isPelindrome(str(multi)):
                if multi>biggest_pelindrome:
                    biggest_pelindrome=multi
                    
    return biggest_pelindrome                





print(BiggestPelindrome(1000))