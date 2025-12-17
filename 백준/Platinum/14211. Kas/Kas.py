import sys
input = sys.stdin.readline

n = int(input())
c = [int(input()) for _ in range(n)]
csum = sum(c)

dp = [-1]*(csum+1)
dp[0] = 0

for x in c:
    dp2 = dp[::]
    for i in range(csum+1):
        if dp[i] == -1:
            continue

        dp2[i+x] = max(dp2[i+x], dp[i] + x)
        dp2[abs(i-x)] = max(dp2[abs(i-x)], dp[i] + x)
    
    dp = dp2

print(dp[0]//2 + csum - dp[0])