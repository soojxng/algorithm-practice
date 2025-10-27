import sys
input = sys.stdin.readline

def is_win(f):
    for i in range(0, 3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == ox[f]:
            return 1
        if board[i] == board[i+3] == board[i+6] == ox[f]:
            return 1
    if board[0] == board[4] == board[8] == ox[f]:
        return 1
    if board[2] == board[4] == board[6] == ox[f]:
        return 1
    return 0

ox = ['O', 'X']
while 1:
    board = input().rstrip()

    if board == 'end':
        break

    o, x = 0, 0
    for b in board:
        if b == 'X':
            x += 1
        elif b =='O':
            o += 1

    f = x - o
    if f not in (0, 1):
        print('invalid')
        continue
    
    ret = [is_win(f), is_win(0 if f else 1)]
    if (ret[0] and not ret[1]) or (not ret[0] and not ret[1] and o+x == 9):
        print('valid')
    else:
        print('invalid')