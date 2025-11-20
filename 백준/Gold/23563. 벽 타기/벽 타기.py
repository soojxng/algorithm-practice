import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
board = [list(input().rstrip()) for _ in range(h)]
dist = [[float('inf')]*w for _ in range(h)]

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
nboard = [[1 for _ in range(w)] for _ in range(h)]
s, e = 0, 0
for i in range(h):
    for j in range(w):
        if board[i][j] == '#':
            dist[i][j] = -1
            for dx, dy in d:
                nx = i + dx
                ny = j + dy
                if 1 <= nx < h-1 and 1 <= ny < w-1 and board[nx][ny] != '#':
                    nboard[nx][ny] = 0
        elif board[i][j] == 'S':
            s = (i, j)
        elif board[i][j] == 'E':
            e = (i, j)

q = deque([(s[0], s[1])])
dist[s[0]][s[1]] = 0
while q:
    x, y = q.popleft()
    if x == e[0] and y == e[1]:
        continue

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nboard[x][y] == nboard[nx][ny] == 0 and dist[x][y] < dist[nx][ny]:
            dist[nx][ny] = dist[x][y]
            q.appendleft((nx, ny))
        elif dist[x][y] + 1 < dist[nx][ny]:
            dist[nx][ny] = dist[x][y]+1
            q.append((nx, ny))

print(dist[e[0]][e[1]])