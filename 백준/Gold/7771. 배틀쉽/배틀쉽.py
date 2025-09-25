import sys
input = sys.stdin.readline

board = [['.']*10 for _ in range(10)]
x = 0
for i in range(10):
    tmp = list(map(int, input().split()))
    for j in range(10):
        if tmp[j] == 100:
            x = i
            board[i][j] = '#'

s = {'####.###.#', '###.##.##.', '##.#.#....'}
for i in range(0, 10, 2):
    if not s:
        break
    if i not in (x-1, x, x+1):
        board[i] = s.pop()

for b in board:
    print(''.join(b))