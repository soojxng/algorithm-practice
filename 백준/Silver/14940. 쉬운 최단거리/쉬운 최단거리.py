import sys
from collections import deque
input = sys.stdin.readline

def find2():
    for i in range(n):
        for j in range(m):
            if graphs[i][j] == 2:
                graphs[i][j] = 0
                return (i, j)

n, m = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d = find2()
results = [[-1 if i else 0 for i in j] for j in graphs]
q = deque([(d[0], d[1], 1)])

while q:
    x, y, cnt = q.popleft()
    for dx, dy in dxy:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < m and graphs[xx][yy]:
            graphs[xx][yy] = 0
            results[xx][yy] = cnt
            q.append((xx, yy, cnt+1))
            
for r in results:
    print(' '.join(map(str, r)))