import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[-1]*(k+1) for _ in range(n)]
dp[-1][0] = 0

for i in range(n):
    wt, wc, bt, bc = map(int, input().split())
    tmp = [-1]*(k+1)
    for t in range(k + 1):
        if dp[i-1][t] != -1:
            if t+wt <= k:
                dp[i][t+wt] = max(dp[i][t+wt], dp[i-1][t] + wc)
            if t+bt <= k:
                dp[i][t+bt] = max(dp[i][t+bt], dp[i-1][t] + bc)
        
print(max(dp[-1]))