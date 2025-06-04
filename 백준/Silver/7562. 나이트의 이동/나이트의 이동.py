import sys
from collections import deque
input = sys.stdin.readline

def bfs(x1, x2, y1, y2, l):
    visited[x1][y1] = 1
    q = deque([(x1, y1, 0)])
    while q:
        x, y, cnt = q.popleft()
        if x == x2 and y == y2:
            print(cnt)
            break
        for dx, dy in d:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < l and 0 <= yy < l and visited[xx][yy] == 0 :
                visited[xx][yy] = 1
                q.append((xx, yy, cnt+1))
      
d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
for _ in range(int(input())):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    bfs(x1, x2, y1, y2, l)