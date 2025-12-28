import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0] = list(map(int, board[0]))

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            continue
        dp[i][j] = int(board[i][j]) if i == 0 or j == 0 else (min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1)
        ans = max(ans, dp[i][j])

print(ans*ans)