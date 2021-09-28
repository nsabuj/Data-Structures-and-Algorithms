# Helper function that allocates a new
# node with the given data and None
# left and right poers.                                
class Node:
 
    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Returns true if given tree is BST.
def isBST(root, left = None, right = None):
    print("root:",root.data) if root !=None else print("root None")
    if left is not None: 
         print("left",left.data) 
    else:
          print("left None")
    if right is not None: 
         print("right",right.data) 
    else:
          print("right None")
    # Base condition
    if (root == None) :
        return True
 
    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (left != None and root.data <= left.data) :
        
        return False
 
    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if (right != None and root.data >= right.data) :
        
        return False
   
    
    # check recursively for every node.

    return isBST(root.left, left, root) and isBST(root.right, root, right)
 
 
# Driver Code
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(12)
    root.right.left = Node(5)
    root.left.right = Node(3)
   
    if (isBST(root,None,None)):
        print("Is BST")
    else:
        print("Not a BST")
 

