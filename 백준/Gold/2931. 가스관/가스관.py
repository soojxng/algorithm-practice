import sys
input = sys.stdin.readline
from collections import deque

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
arr = [{'|', '+', '2', '3'}, {'-', '+', '3', '4'}, {'|', '+', '1', '4'}, {'-', '+', '1', '2'}]
road = {0b1111: '+', 0b1010: '|', 0b0101: '-', 0b1100: 1, 0b0110: 2, 0b0011: 3, 0b1001: 4}
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
ans = 0
tmp = 0
for i in range(r):
    if ans:
        break
    for j in range(c):
        tmp = 0
        if board[i][j] == '.':
            for k in range(4):
                nx, ny = i+d[k][0], j+d[k][1]
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] in arr[k]:
                    tmp |= (1 << (3-k))
        if tmp > 0:
            ans = [i+1, j+1, road[tmp]]
            break

print(*ans)