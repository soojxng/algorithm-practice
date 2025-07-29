import sys
input = sys.stdin.readline

n, m, c0, d0 = map(int, input().split())
dp = [0]*(n+1)

for i in range(c0, n+1):
    dp[i] = dp[i-c0] + d0
    
for _ in range(m):
    a, b, c, d = map(int, input().split())
    cnt = min(a//b, n//c)
    k = 1
    while cnt > 0:
        tmp = min(k, cnt)
        f = c * tmp
        cost = d * tmp
        for i in range(n, f-1, -1):
            dp[i] = max(dp[i], dp[i-f]+cost)
        cnt -= tmp
        k *= 2
print(dp[-1])