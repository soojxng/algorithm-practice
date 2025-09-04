import sys
input = sys.stdin.readline
import heapq
from collections import deque

n, m = map(int, input().split())
maps = [[] for _ in range(n)]
q = deque()
V = []
J = []
d = ((-1, 0), (0, -1), (1, 0), (0, 1))
dist = [[float('inf')]*m for _ in range(n)]

for i in range(n):
    maps[i] = list(input().rstrip())
    for j in range(m):
        if maps[i][j] == '+':
            dist[i][j] = 0
            q.append((i, j, 0))
        elif maps[i][j] == 'V':
            V = (i, j)
        elif maps[i][j] == 'J':
            J = (i, j)

#칸별 나무와 거리 최솟값 구하기
while q:
    x, y, cnt = q.popleft()
    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] > cnt+1:
            dist[nx][ny] = cnt + 1
            q.append((nx, ny, cnt+1))

#가장 안전한 길 구하기
ans = 0
h = []
heapq.heappush(h, (-dist[V[0]][V[1]], V[0], V[1]))
dist2 = [[-1]*m for _ in range(n)]
dist2[V[0]][V[1]] = dist[V[0]][V[1]]

while h:
    cnt, x, y = heapq.heappop(h)
    cnt = -cnt
    if (x, y) == J:
        ans = max(ans, cnt)
        continue
    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] != 0:
            tmp = min(cnt, dist[nx][ny])
            if tmp > dist2[nx][ny]:
                dist2[nx][ny] = cnt
                heapq.heappush(h, (-tmp, nx, ny))

print(ans)