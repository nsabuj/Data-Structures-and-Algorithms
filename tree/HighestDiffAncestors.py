class Solution:
    def __init__(self):
        self.res=0
        
    def DFS(self,node,min_val,max_val):
        if node==None:
            return 
        self.res=max(self.res,abs(node.val-min_val),abs(node.val-max_val))
        min_val=min(min_val,node.val)
        max_val=max(max_val,node.val)
        self.DFS(node.left,min_val,max_val)
        self.DFS(node.right,min_val,max_val)

        
    def maxAncestorDiff(self, root):

       
        
        self.DFS(root,root.val,root.val)        
        return self.res 