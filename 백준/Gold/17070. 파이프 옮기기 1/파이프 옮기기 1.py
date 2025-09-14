import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for x in range(n):
    for y in range(2, n):
        if house[x][y] == 1:
            continue

        if house[x][y-1] == 0:
            dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][1]

        if x > 0 and house[x-1][y] == 0:
            dp[x][y][2] = dp[x-1][y][1] + dp[x-1][y][2]

        if x > 0 and house[x-1][y] == 0 and house[x][y-1] == 0 and house[x-1][y-1] == 0:
            dp[x][y][1] = sum(dp[x-1][y-1])

print(sum(dp[n-1][n-1]))