import collections
# Python3 program to implement
# the above approach
 
# Stores the adjacency list
vec = collections.defaultdict(list)
 
# Stores if a vertex is
# visited or not
vis = {}

 
# Function to perform DFS Traversal
# to count the number and size of
# all connected components
def dfs(node):
     
 
     
    # Mark the current node as visited

    vis[node] = True
    
    # Traverse the adjacency list
    # of the current node
    for x in vec[node]:
 
        # For every unvisited node
        if (x not in vis):
#if (vis[x] == 0):           
 
            # Recursive DFS Call
            
            dfs(x)
 
# Function to add undirected
# edge in the graph
def addEdge(u, v):
     
    vec[u].append(v)
    vec[v].append(u)
 
# Function to calculate minimum
# number of edges to be removed
def minEdgeRemoved(N, M, Edges):
     
    
 
    # Create Adjacency list
    for i in range(M):
        addEdge(Edges[i][0], Edges[i][1])
 
    # memset(vis, false, sizeof(vis))
    k = 0
 
    # Iterate over all the nodes
#    for key in range(1, N + 1):
#        if (not vis[key]): 
    for key in vec.keys():
        
        if (key not in vis):
            
            dfs(key)
            k += 1
 
    # Print the final count
   
    print(M - N + k)
 
# Driver Code
if __name__ == '__main__':
     
    N = 4
    M = 6
 
    Edges = [['A', 'B'], ['B', 'C'],['C','D'],['A','C'],['A','D'],['B','D']]
 
    minEdgeRemoved(N, M, Edges)