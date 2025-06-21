import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for l in range(1, N):
    for i in range(N-l):
        j = i+l
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1])
            
print(dp[0][-1])