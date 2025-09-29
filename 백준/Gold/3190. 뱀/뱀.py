import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = -1

l = int(input())
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
moving = dict()
tmp = 0
for i in range(l):
    x, c = input().split()
    tmp = (tmp + (-1 if c == 'L' else 1)) % 4
    moving[int(x)] = tmp

snake = deque([(0, 0)])
board[0][0] = 1
cnt = 0
c = 0
s = set(moving.keys())
while 1:
    if cnt in s:
        c = moving[cnt]
    cnt += 1
    x, y = snake[-1]
    nx, ny = x + d[c][0], y + d[c][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break
    if board[nx][ny] == 1:
        break
    if board[nx][ny] == 0:
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    snake.append((nx, ny))
    board[nx][ny] = 1

print(cnt)