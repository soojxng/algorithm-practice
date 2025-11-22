import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*21 for _ in range(n-1)]
dp[0][nums[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        x = nums[i]
        if 0 <= j - x:
            dp[i][j] += dp[i-1][j-x]
        if j + x <= 20:
            dp[i][j] += dp[i-1][j+x]

print(dp[-1][nums[-1]])