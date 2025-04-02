import sys
input = sys.stdin.readline

N = int(input())

a = [int(input()) for _ in range(N)]
b = [0] * N
    
if N < 3:
    print(sum(a))
    
else:    
    b[0] = a[0]
    b[1] = b[0] + a[1]
    
    for i in range(2, N):
        b[i] = max(b[i-2] + a[i], b[i-3] + a[i-1] + a[i])
    
    print(b[-1])