import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[[] for _ in range(m+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if a[i] == b[j]:
            tmp = [a[i]] + dp[i+1][j+1]
        else:
            tmp = []
        dp[i][j] = max(tmp, dp[i+1][j], dp[i][j+1])

print(len(dp[0][0]))
if dp[0][0]:
    print(*dp[0][0])