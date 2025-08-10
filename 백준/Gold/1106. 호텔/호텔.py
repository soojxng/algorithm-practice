import sys
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [float('inf')]*(c+101)
dp[0] = 0
for i in range(n):
    a, b = map(int, input().split())
    for i in range(b, c+101):
        dp[i] = min(dp[i], dp[i-b]+a)
print(min(dp[c:]))