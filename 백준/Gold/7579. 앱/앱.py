N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
ans = float('inf')
dp = [[0]*(sum(costs)+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(sum(costs)+1):
        if j < costs[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-costs[i-1]] + memories[i-1], dp[i-1][j])
        if dp[i][j] >= M: ans = min(ans, j)
        
print(ans)