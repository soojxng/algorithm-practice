import sys
input = sys.stdin.readline

MOD = 1000000003
n = int(input())
k = int(input())

if k > n//2:
    print(0)
else:
    dp = [[0]*(k+1) for _ in range(n)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, n):
        dp[i][0] = 1
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD
    print((dp[n-1][k] + dp[n-3][k-1]) % MOD)