    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        s=list(s)
        if len(s)<1:
            return 0
        total=0
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)
            elif s[i]==")":
                if len(stack)<1:
                    
                    total+=1
                else:
                    stack.pop()


        total+=len(stack)
        return total   