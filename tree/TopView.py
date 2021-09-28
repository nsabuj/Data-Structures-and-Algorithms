class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.horiz_dis=0


def topViewIterative(node):
    if node==None:
        return

    qu=[]
    
    horiz_dis=0
    node.horiz_dis=horiz_dis
    qu.append(node)
    m=dict()    #Hashmap to store horizontal distances of tree


    while qu:
        current_node=qu[0]
        horiz_dis=current_node.horiz_dis
        if horiz_dis not in m:                #
            m[horiz_dis]=current_node.data
        if current_node.left:
            current_node.left.horiz_dis=horiz_dis-1
            qu.append(current_node.left)
        if current_node.right:
            current_node.right.horiz_dis=horiz_dis+1
            qu.append(current_node.right)
        qu.pop(0)
          
    for i in sorted(m):
        print(m[i],end=" ")

        

def fillMap(root, distance, level, m):
    if(root == None):
        return
 
    if distance not in m:
        m[distance] = [root.data, level]
    elif(level>=m[distance][1]):
        m[distance] = [root.data, level]
    fillMap(root.left, distance - 1, level + 1, m)
    fillMap(root.right, distance + 1, level + 1, m)
 
# function should prthe topView of
# the binary tree
 
 
def BottomViewRecursive(root):
 
    # map to store the pair of node value and its level
    # with respect to the vertical distance from root.
    m = {}
 
    fillMap(root, 0, 0, m)
    
    for it in sorted(m.keys()):
        print(m[it][0], end=" ")



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
     
topViewIterative(root)
print("\n")
BottomViewRecursive(root)


