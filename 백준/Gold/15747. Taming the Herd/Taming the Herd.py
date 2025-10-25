import sys
input = sys.stdin.readline

INF = float('inf')
n = int(input())
log = list(map(int, input().split()))

dp = [[[INF]*(n+1) for _ in range(n+1)] for _ in range(n)]

dp[0][1][0] = 0 if log[0] == 0 else 1

for i in range(1, n):
    for j in range(1, i+2):
        for k in range(n):
            if dp[i-1][j][k] == INF:
                continue
            if j + 1 <= n:
                dp[i][j+1][0] = min(dp[i][j+1][0], dp[i-1][j][k] + (0 if log[i] == 0 else 1))
            if k + 1 <= n:
                dp[i][j][k+1] = min(dp[i][j][k+1], dp[i-1][j][k] + (0 if log[i] == k+1 else 1))

for x in range(1, n+1):
    print(min(dp[n-1][x]))