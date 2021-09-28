# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def DFS(node,count):
    if node==None:
        return count
    count+=1
    return max(DFS(node.left,count),DFS(node.right,count))
        
def maxDepth(root): 
    return DFS(root,0)




tree_to_travel=[3,9,20,None,None,15,7]
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.left.left=TreeNode(None)
root.left.right=TreeNode(None)
root.right.left=TreeNode(15)
root.right.right=TreeNode(17)    
print(maxDepth(root))

