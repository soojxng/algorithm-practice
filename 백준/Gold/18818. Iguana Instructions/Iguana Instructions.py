import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = [list(input().rstrip()) for _ in range(n)]
visited = [[float('inf') if maps[i][j] == '.' else -1 for j in range(n)] for i in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = deque()
q.append((0, 0, -1, 0))
visited[0][0] = 1
while q:
    x, y, di, cnt = q.popleft()
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if i == di and visited[nx][ny] >= cnt:
                visited[nx][ny] = cnt
                q.append((nx, ny, i, cnt))
            elif i != di and visited[nx][ny] >= cnt+1:
                visited[nx][ny] = cnt+1
                q.append((nx, ny, i, cnt+1))
print(visited[-1][-1])