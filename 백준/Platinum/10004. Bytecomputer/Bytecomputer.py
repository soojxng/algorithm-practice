import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [[float('inf')]*3 for _ in range(n)]
dp[0][a[0]+1] = 0

for i in range(1, n):
    if dp[i-1][0] == dp[i-1][1] == dp[i-1][2] == float('inf'):
        break
    dp[i][0] = dp[i-1][0] + a[i] + 1
    dp[i][1] = min(dp[i-1][0] if a[i] == 0 else float('inf'),
                   dp[i-1][1] if a[i] == 0 else float('inf'),
                   dp[i-1][0] + 1 if a[i] == 1 else float('inf'))
    dp[i][2] = min(min(dp[i-1]) if a[i] == 1 else float('inf'),
                   dp[i-1][2] + 1 - a[i])

ans = min(dp[n-1])
print(ans if ans < float('inf') else 'BRAK')