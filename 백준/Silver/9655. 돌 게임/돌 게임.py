n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n >= 3: dp[3] = 1
for i in range(4, n+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1
print('SK' if dp[n] else 'CY')