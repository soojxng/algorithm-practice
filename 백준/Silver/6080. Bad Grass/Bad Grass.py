import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
grass = [list(map(int, input().split())) for _ in range(r)]
visited = [[1 if grass[i][j] == 0 else 0 for j in range(c)] for i in range(r)]
d = [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-1, -1), (-1, 0), (-1, 1)]
q = deque()
cnt = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            q.append((i, j))
            cnt += 1
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
print(cnt)