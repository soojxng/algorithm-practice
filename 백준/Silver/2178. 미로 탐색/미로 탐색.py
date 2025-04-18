import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for __ in range(N)]
        
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque([(0, 0, 1)])

while q:
    x, y, cnt = q.popleft()
    if x == N-1 and y == M-1:
        print(cnt)
    for dx, dy in d:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < N and 0 <= yy < M and maps[xx][yy]:
            maps[xx][yy] = 0
            q.append((xx, yy, cnt + 1))
    cnt += 1