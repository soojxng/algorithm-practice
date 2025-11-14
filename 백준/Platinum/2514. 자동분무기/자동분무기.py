import sys
input = sys.stdin.readline

m = int(input())
k = int(input())
board = [list(map(int, input().split())) for _ in range(8)]
rsum = [0]*8
csum = [0]*8

for i in range(8):
    for j in range(8):
        board[i][j] -= m
        rsum[i] += board[i][j]
        csum[j] += board[i][j]

tot = sum(rsum) // 15
rsum = [(r-tot) // 7 for r in rsum]
csum = [(c-tot) // 7 for c in csum]

ans = [['.']*8 for _ in range(8)]
tot /= 15
for i in range(8):
    for j in range(8):
        x = rsum[i] + csum[j] - board[i][j]
        if x == 1:
            ans[i][j] = '+'
        elif x == -1:
            ans[i][j] = '-'

for a in ans:
    print(*a)