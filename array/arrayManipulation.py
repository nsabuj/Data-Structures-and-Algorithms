import itertools, sys
def ArrayManupulation(n,queries):
    N, M = n,queries
    x = [0] * N

    for i in range(len(M)):
        a, b, k = M[i]

        x[a - 1] += k
        if b < N:
            x[b] -= k

            
    return max(itertools.accumulate(x))

if __name__=='__main__' :
    queries=[[1, 5 ,3],
    [4 ,8 ,7],
    [6, 9, 1]]
    print(ArrayManupulation(10,queries))




