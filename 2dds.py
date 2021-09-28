import sys
def hourglassSum(arr):
    # Write your code here
    sum_of_hourglasses=[]
    max_value=None
    for row in range(4):
        
        for col in range(4):
            sum=arr[row][col]+arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1]+arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
            if max_value==None or sum>max_value:
                max_value=sum

            
    return max_value   



if __name__ == '__main__':

        d = sys.stdin.read().splitlines()
        d = [list(map(int,i.split())) for i in d]
            
        result = hourglassSum(d)
        print(result)

