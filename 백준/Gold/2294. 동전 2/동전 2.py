import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    c = int(input())
    if c <= k:
        coins.append(c)
        
dp = [float('inf')]*(k+1)
for c in coins:
    dp[c] = 1

for c in coins:
    for i in range(c+1, k+1):
        dp[i] = min(dp[i-c]+1, dp[i])
        
print(dp[k] if dp[k] != float('inf') else -1)