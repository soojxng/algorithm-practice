import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
rooms = [list(input().rstrip()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

q = deque([(0, 0, 0)])
visited[0][0] = True
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

while q:
    cnt, x, y = q.popleft()
    if x == m-1 and y == n-1:
        print(cnt)
        break

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if rooms[nx][ny] == '1':
                q.append((cnt+1, nx, ny))
            else:
                q.appendleft((cnt, nx, ny))