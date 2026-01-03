import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
if n >= 2: dp[2] = 3
tmp = 1
for i in range(4, n+1, 2):
    dp[i] = (3 * dp[i-2]) + (2 * tmp)
    tmp += dp[i-2]

print(dp[n])