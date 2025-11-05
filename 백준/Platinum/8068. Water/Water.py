import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
h = []
if n > 1 and m > 1:
    for i in range(0, n, n-1):
        for j in range(m):
            heapq.heappush(h, (board[i][j], i, j))
            visited[i][j] = True

    for i in range(1, n-1):
        for j in range(0, m, m-1):
            heapq.heappush(h, (board[i][j], i, j))
            visited[i][j] = True

d = ((-1, 0), (0, -1), (1, 0), (0, 1))
ans = 0
while h:
    height, x, y = heapq.heappop(h)
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            ans += max(0, height - board[nx][ny])
            heapq.heappush(h, (max(board[nx][ny], height), nx, ny))
            visited[nx][ny] =True

print(ans)