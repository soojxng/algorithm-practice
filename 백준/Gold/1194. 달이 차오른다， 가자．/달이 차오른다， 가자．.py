import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
s = 0
e = set()
for i in range(n):
    for j in range(m):
        if maze[i][j] == '0':
            s = (i, j)
        elif maze[i][j] == '1':
            e.add((i, j))

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
ind = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
visited[s[0]][s[1]][0] = 1
q = deque([(s[0], s[1], 0, 0)]) #x, y, z, cnt

ans = -1
while q:
    x, y, z, cnt = q.popleft()
    if (x, y) in e:
        ans = cnt
        break

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        nz = z
        if 0 <= nx < n and 0 <= ny < m:
            nxt = maze[nx][ny]
            if nxt == '#':
                continue
            elif nxt in ('A', 'B', 'C', 'D', 'E', 'F') and nz & (1 << ind[nxt]) == 0:
                continue
            elif nxt in ('a', 'b', 'c', 'd', 'e', 'f'):
                nz |= (1 << ind[nxt])
            if visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = 1
                q.append((nx, ny, nz, cnt + 1)) 

print(ans)