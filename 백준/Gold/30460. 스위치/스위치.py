import sys
input = sys.stdin.readline
    
n = int(input())
a = list(map(int, input().split()))
dp = [-float('inf')]*n
tmp = a[0] + a[1] + a[2]
dp[0] = a[0]
dp[1] = dp[0] + a[1]
dp[2] = max(dp[1] + a[2], tmp*2)

for i in range(3, n):
    tmp = tmp - a[i-3] + a[i]
    dp[i] = max(dp[i-1] + a[i], dp[i-3] + (tmp*2))

print(max(dp[n-1], dp[n-3] + (a[-2] + a[-1])*2, dp[n-2] + (a[-1]*2)))