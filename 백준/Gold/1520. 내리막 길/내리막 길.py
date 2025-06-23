import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[x][y]:
            dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]

M, N = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(M))
dp = [[-1]*N for m in maps]
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

print(dfs(0, 0))