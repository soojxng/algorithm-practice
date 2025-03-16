import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n, k = 1, 1
for i in range(1, K+1):
    k *= i
for j in range(N, N-K, -1):
    n *= j
     
print(n//k)