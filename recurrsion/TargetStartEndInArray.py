def BinarySearch(nums,left, right,target):
    mid=0
    while left<=right:
        
        mid=left+right//2
 

        if nums[mid]==target:
             return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1   

    
    
               
def searchRange( nums, target):
        first_pos=BinarySearch(nums,0,len(nums)-1,target)
        if first_pos==-1:
            return [-1,-1]
        end_pos=first_pos
        start_pos=first_pos
        temp_left=0
        temp_right=0
        
        while start_pos!=-1:
            
            temp_left=start_pos
            start_pos=BinarySearch(nums,0,start_pos-1,target)
           
            
        start_pos=temp_left
        
        while end_pos!=-1:
            
            temp_right=end_pos
            end_pos=BinarySearch(nums,end_pos+1,len(nums)-1,target)
        end_pos=temp_right
        
        return [start_pos,end_pos]


print(searchRange([5,7,7,8,8,10],8))
