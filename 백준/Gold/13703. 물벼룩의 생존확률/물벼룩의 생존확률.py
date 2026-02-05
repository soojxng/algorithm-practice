import sys
input = sys.stdin.readline

k, n = map(int, input().split())
dp = [[0]*128 for _ in range(64)]
dp[0][k] = 1
for i in range(1, n+1):
    for j in range(1, 127):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) if k != 0 else 0)