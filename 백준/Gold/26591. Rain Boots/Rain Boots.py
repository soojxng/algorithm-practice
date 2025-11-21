import sys
lines = sys.stdin.readlines()
from collections import deque

for k in range(0, len(lines), 9):
    board = [list(lines[k+l].rstrip()) for l in range(8)]
    dist = [[float('inf')]*8 for _ in range(8)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    s, e = 0, 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'S':
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
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] != 'M' and dist[x][y] < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                elif board[nx][ny] == 'M' and dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx, ny))

    print(dist[e[0]][e[1]])