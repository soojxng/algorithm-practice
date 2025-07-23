import sys
input = sys.stdin.readline
from collections import deque

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)
    
def bfs(a, b, num):
    q = deque([(a, b)])
    maps[a][b] = num
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = dx+x
            ny = dy+y
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = num
                q.append((nx, ny))
                
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num = 2
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            bfs(i, j, num)
            num += 1
parents = [i for i in range(num)]
edges = []
for i in range(n):
    for j in range(m):
        if maps[i][j] > 0:
            for dx, dy in ((0, 1), (1, 0)):
                cnt = 0
                nx = i + dx
                ny = j + dy
                while nx < n and ny < m and maps[nx][ny] == 0:
                    cnt += 1
                    nx += dx
                    ny += dy
                if cnt > 1 and nx < n and ny < m and maps[nx][ny] != maps[i][j]:
                    edges.append((cnt, maps[i][j], maps[nx][ny]))
edges.sort()
ans = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
roots = set(find(i) for i in range(2, num))
if len(roots) != 1:
    print(-1)
else:
    print(ans)