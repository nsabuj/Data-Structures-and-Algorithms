    def countNodes(self, root):
        if root==None:
            return 0

        RightHeight=0
        LeftHeight= 0
        LeftTree=root
        RightTree=root
        while(LeftTree!=None):
            LeftHeight+=1
            LeftTree=LeftTree.left
            
        while RightTree!= None:
            RightHeight+=1
            RightTree=RightTree.right
            
        if RightHeight==LeftHeight:
            return 2**RightHeight-1
        
        return self.countNodes(root.left) + self.countNodes(root.right)+1 