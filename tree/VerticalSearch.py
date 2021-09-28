import heapq
# Python program for printing vertical order of a given
# binary tree
 
# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
 
# Utility function to store vertical order in map 'm'
# 'hd' is horizontal distance of current node from root
# 'hd' is initially passed as 0

            
def verticalTraversal( node):

    if node==None:
        return

    qu=[]
    
    horiz_dis=0
    node.horiz_dis=horiz_dis
    qu.append(node)
    m=dict()    #Hashmap to store horizontal distances of tree

    qusize=len(qu)

    while qu:
        qusize=len(qu)
        if qusize>0:
           qu.sort(key=lambda x: x.val, reverse=False)     #sorting inside level 

        i=0
        while i<qusize:                      # continue until the end of the level
            current_node=qu.pop(0)
            
            horiz_dis=current_node.horiz_dis
                
            try:
                m[horiz_dis].append(current_node.val)
            except:
                m[horiz_dis]=[current_node.val]

            if current_node.left:
                current_node.left.horiz_dis=horiz_dis-1
                qu.append(current_node.left)
            if current_node.right:
                current_node.right.horiz_dis=horiz_dis+1
                qu.append(current_node.right)
            
            i+=1  
    values=[m[i] for i in sorted(m.keys())]
    return values
    
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)


print(verticalTraversal(root))


