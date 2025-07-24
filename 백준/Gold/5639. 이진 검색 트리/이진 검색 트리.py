import sys
sys.setrecursionlimit(100000)

def find_post(i, j):
    if i >= j:
        return
    l = j
    for k in range(i+1, j):
        if A[k] > A[i]:
            l = k
            break
    
    find_post(i+1, l)
    find_post(l, j)
    print(A[i])

A = [int(s) for s in sys.stdin.readlines()]
find_post(0, len(A))