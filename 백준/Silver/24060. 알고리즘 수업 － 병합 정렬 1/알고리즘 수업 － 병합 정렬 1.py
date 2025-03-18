import sys
input = sys.stdin.readline

def merge_sort(A):
    if len(A) <= 1: return A
    q = (len(A)+1) // 2
    l = merge_sort(A[:q])
    r = merge_sort(A[q:])

    return merge(l, r)

def merge(A, B):
    C = []
    i, j = 0, 0
    global cnt, x, K
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            tmp = A[i]
            i += 1
        else:
            tmp = B[j]
            j += 1
            
        cnt += 1
        if cnt == K:
            x = tmp
        C.append(tmp)
            
    tmp = A[i:] + B[j:]
    if cnt < K <= cnt + len(tmp):
        x = tmp[K - cnt - 1]
    cnt += len(tmp)
    return C + tmp

global cnt, x, K
N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
x = -1
A = merge_sort(A)
print(x)