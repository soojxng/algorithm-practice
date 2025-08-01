import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maps = list(list(input().rstrip()) for _ in range(n))
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

visited = [[[0]*4 for i in range(m)] for j in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == '#':
            visited[i][j] = [1, 1, 1, 1]
        elif maps[i][j] == 'W':
            q.append((i, j))
            visited[i][j] = [1, 1, 1, 1]

while q:
    x, y = q.popleft()
    
    for k in range(4):
        dx = x + d[k][0]
        dy = y + d[k][1]
        
        if visited[dx][dy][k] == 0:
            if maps[dx][dy] == '.' or maps[dx][dy] == 'W':
                visited[dx][dy] = [1, 1, 1, 1]
                q.append((dx, dy))
                
            elif maps[dx][dy] == '+':
                while 1:
                    visited[dx][dy][k] = 1
                    nx = dx + d[k][0]
                    ny = dy + d[k][1]
                    if maps[nx][ny] == '#':
                        q.append((dx, dy))
                        break
                    if (maps[nx][ny] == '.' or maps[nx][ny] == 'W') and visited[nx][ny][k] == 0:
                        visited[nx][ny] = [1,1,1,1]
                        q.append((nx, ny))
                        break
                    dx, dy = nx, ny

for i in range(n):
    s = ''
    for j in range(m):
        if maps[i][j] == '.' and visited[i][j][0] == 0:
            s += 'P'
        else:
            s += maps[i][j]
    print(s)