# Python3 program to find 
# minimum number of swaps
# required to sort an array
 
# Function returns the minimum
# number of swaps required to
# sort the array
def minSwaps(arr):
    n = len(arr)
     
    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]
     
    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key = lambda it : it[1])
     
    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k : False for k in range(n)}
     
    # Initialize result
    ans = 0
    for i in range(n):
         
        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue
             
        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
         
        while not vis[j]:
             
            # mark node as visited
            vis[j] = True
             
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
             
        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
             
    # return answer
    return ans



def minimumBrives(Q):
 #
    # initialize the number of moves
    moves = 0 
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P-1 for P in Q]
    
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):
        print(i)
        print(P)
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of 
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1

    return moves


if __name__ == '__main__':
    result = minimumBrives([1, 2, 5, 3, 7, 8, 6, 4])
    print(result)    