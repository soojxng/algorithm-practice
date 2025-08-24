import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0]*(b+1) for _ in range(a+1)]
path = [[0]*(b+1) for _ in range(a+1)]
for i in range(1, a+1):
    path[i][0] = 1
for j in range(1, b+1):
    path[0][j] = 2
for i in range(1, a+1):
    for j in range(1, b+1):
        x, y, z = dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + score[A[i-1]-1][B[j-1]-1]
        dp[i][j] = max(x, y, z)
        if dp[i][j] == x:
            path[i][j] = 1
        elif dp[i][j] == y:
            path[i][j] = 2
        elif dp[i][j] == z:
            path[i][j] = 3
            
print(dp[a][b])
ans = []
while a != 0 or b != 0:
    ans.append(path[a][b])
    if path[a][b] == 1:
        a -= 1
    elif path[a][b] == 2:
        b -= 1
    elif path[a][b] == 3:
        a -= 1
        b -= 1
print(*reversed(ans))