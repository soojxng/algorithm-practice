import sys
from collections import deque
input = sys.stdin.readline

def find(N, visited, flag):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == flag:
                return (i, j)
    return 0
                        
N = int(input())
colors = [input().strip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
rg = set(['R', 'G'])
cnt = [0, 0]
        
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque()

while 1:
    tmp = find(N, visited, 0)
    if tmp == 0:
        break
    else:
        q.append(tmp)
        visited[tmp[0]][tmp[1]] = 1
        cnt[0] += 1
    while q:
        x, y = q.popleft()
        c = colors[x][y]
        for dx, dy in d:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < N and 0 <= yy < N and c == colors[xx][yy] and visited[xx][yy] == 0:
                    q.append((xx, yy))
                    visited[xx][yy] = 1

while 1:
    tmp = find(N, visited, 1)
    if tmp == 0:
        break
    else:
        q.append(tmp)
        visited[tmp[0]][tmp[1]] = 0
        cnt[1] += 1
    while q:
        x, y = q.popleft()
        c = colors[x][y]
        for dx, dy in d:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < N and 0 <= yy < N and visited[xx][yy]:
                if c in rg and colors[xx][yy] in rg:
                    q.append((xx, yy))
                    visited[xx][yy] = 0
                elif c == colors[xx][yy] == 'B':
                    q.append((xx, yy))
                    visited[xx][yy] = 0
                    
print(' '.join(map(str, cnt)))