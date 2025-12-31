import sys
input = sys.stdin.readline

n = int(input())
pins = [tuple(map(int, input().split())) for _ in range(n)]
pins.sort()

dp = [[1]*4 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if pins[i][0] == pins[j][0]:
            continue
        elif pins[i][1] > pins[j][1]:
            dp[i][0] = max(dp[i][0], dp[j][0]+1)
        elif pins[i][1] < pins[j][1]:
            dp[i][1] = max(dp[i][1], dp[j][1]+1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if pins[i][0] == pins[j][0]:
            continue
        elif pins[i][1] > pins[j][1]:
            dp[i][2] = max(dp[i][2], dp[j][2]+1)
        elif pins[i][1] < pins[j][1]:
            dp[i][3] = max(dp[i][3], dp[j][3]+1)

ans = -1
for i in range(n):
    if min(dp[i]) < 2:
        continue
    ans = max(ans, sum(dp[i])-3)

print(ans if ans == -1 else n - ans)