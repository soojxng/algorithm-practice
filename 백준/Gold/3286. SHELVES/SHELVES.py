import sys
input = sys.stdin.readline

c, r = map(int, input().split())
n = int(input())
height = [0]*c
dp = [0]*(c+1)

for _ in range(n):
    a, b = map(int, input().split())
    height[a-1] = max(height[a-1], b)

for i in range(1, c+1):
    dp[i] = dp[i-1] + height[i-1]
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + max(height[i-2], height[i-1]))
    if i >= 3:
        dp[i] = min(dp[i], dp[i-3] + max(height[i-3], height[i-2], height[i-1]))

print(dp[-1])