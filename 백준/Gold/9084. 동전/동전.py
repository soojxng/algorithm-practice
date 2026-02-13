import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(n):
        c = coins[i]
        for j in range(m+1):
            if j >= c:
                dp[j] += dp[j-c]
    print(dp[-1])