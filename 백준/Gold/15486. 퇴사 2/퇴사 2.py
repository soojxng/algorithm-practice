import sys
input = sys.stdin.readline

n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    t, p = a[i]
    dp[i] = max((dp[i + t] + p) if i+t <= n else 0, dp[i+1])

print(dp[0])