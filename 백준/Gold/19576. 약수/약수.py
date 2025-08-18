import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
dp = [0]*N

for i in range(N):
    for j in range(i+1, N):
        if A[j] % A[i] == 0:
            dp[j] = max(dp[j], dp[i]+1)

print(N - max(dp) - 1)