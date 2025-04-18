import sys
from collections import deque
input = sys.stdin.readline

def findHouse():
    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                maps[i][j] = 0
                return (i, j)

N = int(input())
maps = [list(map(int, input().strip())) for __ in range(N)]
        
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque()
houses = []

while sum(sum(m) for m in maps):
    houses.append(1)
    q.append(findHouse())    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < N and 0 <= yy < N and maps[xx][yy]:
                q.append((xx, yy))
                maps[xx][yy] = 0
                houses[-1] += 1

print(len(houses))
for h in sorted(houses):
    print(h)