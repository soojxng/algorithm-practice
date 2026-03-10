import sys
import heapq
input = sys.stdin.readline

t = 0
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

while 1:
    n = int(input())
    if n == 0:
        break
    t += 1

    board = [list(map(int, input().split())) for _ in range(n)]
    h = [(board[0][0], 0, 0)]
    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = 0

    while h:
        w, x, y = heapq.heappop(h)
        if x == n-1 and y == n-1:
            print(f"Problem {t}: {w}")
            break

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nw = w + board[nx][ny]
                if nw < visited[nx][ny]:
                    visited[nx][ny] = nw
                    heapq.heappush(h, (nw, nx, ny))