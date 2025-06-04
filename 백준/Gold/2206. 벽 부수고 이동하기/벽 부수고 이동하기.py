import sys
from collections import deque
input = sys.stdin.readline
 
N, M = map(int, input().split()) 
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
q = deque([(0, 0, 1, 1)])
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while q:
    x, y, cnt, f = q.popleft()
    if x == N-1 and y == M-1:
        print(cnt)
        break
    for dx, dy in d:
        xx = x+dx
        yy = y+dy
        if 0 <= xx < N and 0 <= yy < M:
            if maps[xx][yy] % 10 == 0 and f:
                maps[xx][yy] += 3
                q.append((xx, yy, cnt+1, f))
            elif maps[xx][yy] % 3 == 0 and f == 0:
                maps[xx][yy] += 10
                q.append((xx, yy, cnt+1, f))
            elif maps[xx][yy] == 1 and f:
                q.append((xx, yy, cnt+1, 0))
                maps[xx][yy] = 11
else: print(-1)