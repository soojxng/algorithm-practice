import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt = 0
f = 1
while f:
    if room[r][c] == 0:
        cnt += 1
        room[r][c] = -1

    for i in range(1, 5):
        dx, dy = dir[d - i]
        nx, ny = r + dx, c + dy
        if 0 <= nx < n and 0 <= ny < m and not room[nx][ny]:
            r, c = nx, ny
            d = (d-i) % 4
            break
    else:
        dx, dy = dir[d]
        nx, ny = r - dx, c - dy
        if (nx < 0 or nx >= n or ny < 0 or ny >= m) or room[nx][ny] == 1:
            f = 0
            break
        else: r, c = nx, ny

print(cnt)