import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K = K if N - K > K else N - K
n, k = 1, 1
for i in range(1, K+1):
    n *= (N + 1 - i)
    k *= i
     
print(n//k)