import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
ground = [[1]*m for _ in range(n)]
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == '*':
            ground[i][j] = 0
r1, c1, r2, c2 = map(int, input().split())

dp = [[[0]*m for i in range(n)] for j in range(t+1)]
dp[0][r1-1][c1-1] = 1
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(1, t+1):
    for j in range(n):
        for k in range(m):
            if ground[j][k] == 0:
                continue                
            for dx, dy in d:
                x = j+dx
                y = k+dy
                if 0 <= x < n and 0 <= y < m and ground[x][y]:
                    dp[i][j][k] += dp[i-1][x][y]
            
print(dp[t][r2-1][c2-1])