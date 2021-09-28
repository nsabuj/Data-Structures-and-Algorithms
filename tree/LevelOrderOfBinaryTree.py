# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    queue=[root]
    result=[]
    if root==None:
        return []
    while queue:
        current_level_nodes=[]
        length=len(queue)
        count=0
        while count<length:
            current_node=queue.pop(0)
            current_level_nodes.append(current_node.val)
            if current_node.left!=None:
                queue.append(current_node.left)
            if current_node.right!=None:
                    queue.append(current_node.right)
            count+=1
        result.append(current_level_nodes) 
    return result    
     #Time complexity O(n)
     #Space complexity O(n)




tree_to_travel=[3,9,20,None,None,15,7]
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.left.left=TreeNode(None)
root.left.right=TreeNode(None)
root.right.left=TreeNode(15)
root.right.right=TreeNode(17)    
print(levelOrder(root))

