import sys
input = sys.stdin.readline
from collections import deque 

d = ((-1, 0), (1, 0), (0, -1), (0, 1))
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0]*(m*2) for _ in range(n)] for _ in range(n)]
q = deque()
if (n > 2 and not maze[n-1][n-1] and not maze[0][0]) or (n == 1 and not maze[0][0]):
    q.append((0, 0, 0))
visited[0][0][0] = 1
ans = -1

while q:
    x, y, cnt = q.popleft()
    if x == y == n-1:
        ans = cnt
        break
    ncnt = cnt + 1
    tmp = ncnt % (m*2)
    f = (cnt % (m*2)) >= m 

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        while f and 0 <= nx < n and 0 <= ny < n and maze[nx][ny]:
            nx = nx + dx
            ny = ny + dy
        if 0 <= nx < n and 0 <= ny < n and not maze[nx][ny] and not visited[nx][ny][tmp]:
            q.append((nx, ny, ncnt))
            visited[nx][ny][tmp] = 1

if ans < 0:
    print(ans)
else:
    print(ans//(m*2)+1, 'sun' if ans%(m*2) < m else 'moon')