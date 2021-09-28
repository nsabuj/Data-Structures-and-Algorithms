def lengthOfLongestSubstring(s):
        if len(s)<=1:
            return len(s)
        longest_substring=0
        left=0
        
        seen={}
        for right in range(0,len(s)):
            current_item=s[right]
           
            if current_item in seen and seen[current_item]>=left:
                left=seen[current_item]+1
           
            seen[current_item]=right
            longest_substring=max(longest_substring,(right-left)+1)  
        print(seen)    
        return longest_substring  


print(lengthOfLongestSubstring("abc abcbb"))
