import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(n)]
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
start = [-1, -1]
end = [-1, -1]
board = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if forest[i][j] == 'S':
            start = (i, j)
        elif forest[i][j] == 'F':
            end = (i, j)
        elif forest[i][j] == 'g':
            board[i][j] = 1
        else:
            for dx, dy in d:
                nx, ny = i+dx, j+dy
                if 0 <= nx < n and 0 <= ny < m and forest[nx][ny] == 'g':
                    board[i][j] = 2
                    break

visited = [[[float('inf')]*2 for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = [0, 0]
h = []
heapq.heappush(h, (0, 0, start[0], start[1]))
ans = []
while 1:
    a, b, x, y = heapq.heappop(h)
    if (x, y) == end:
        ans = (a, b)
        break

    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            na, nb = a, b
            if board[nx][ny] == 1:
                na += 1
            elif board[nx][ny] == 2:
                nb += 1
            if [na, nb] < visited[nx][ny]:
                visited[nx][ny][0] = na
                visited[nx][ny][1] = nb
                heapq.heappush(h, (na, nb, nx, ny))

print(*ans)