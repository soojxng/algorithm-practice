n = int(input())
dp = [1, 1, 5, 11]

for i in range(4, n+1):
    dp.append((dp[i-1] + (5*dp[i-2] + dp[i-3] - dp[i-4])) % 1000)

print(dp[n])