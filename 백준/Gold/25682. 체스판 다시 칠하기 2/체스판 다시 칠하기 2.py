import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
board = [[1 if ((i+j) % 2 == 0 and board[i][j] == 'B') or ((i+j) % 2 == 1 and board[i][j] == 'W') else 0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        a = board[i-1][j] if i-1 >= 0 else 0
        b = board[i][j-1] if j-1 >= 0 else 0
        c = board[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
        board[i][j] = board[i][j] + a + b - c
m = float('inf')
for x in range(0, N-K+1):
    if m == 0: break
    for y in range(0, M-K+1):
        a = board[x-1][y+K-1] if x-1 >= 0 else 0
        b = board[x+K-1][y-1] if y-1 >= 0 else 0
        c = board[x-1][y-1] if x-1 >= 0 and y-1 >= 0 else 0
        tmp = board[x+K-1][y+K-1] - a - b + c
        m = min(m, tmp, K*K-tmp)
        
print(m)