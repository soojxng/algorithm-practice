import sys
input = sys.stdin.readline

def cal(board, cnt):
    if cnt == 5:
        global ans
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return
    
    for d in range(4):
        if d > 0:
            board = list(map(list, zip(*board[::-1])))
        b2 = [[0]*n for _ in range(n)]
        for i in range(n):
            tmp = 0
            k = 0
            for j in range(n):
                if board[i][j] == 0:
                    continue
                elif tmp == 0:
                    tmp = board[i][j]
                elif tmp == board[i][j]:
                    b2[i][k] = tmp*2
                    tmp = 0
                    k += 1
                else:
                    b2[i][k] = tmp
                    tmp = board[i][j]
                    k += 1
            if tmp:
                b2[i][k] = tmp
        cal(b2, cnt+1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cal(board, 0)
print(ans)