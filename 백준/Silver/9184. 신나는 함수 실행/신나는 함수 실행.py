import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return W[20][20][20]
    return W[a][b][c]

W = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                W[i][j][k] = 1
            elif i < j < k:
                W[i][j][k] = W[i][j][k-1] + W[i][j-1][k-1] - W[i][j-1][k]
            else:
                W[i][j][k] = W[i-1][j][k] + W[i-1][j-1][k] + W[i-1][j][k-1] - W[i-1][j-1][k-1]

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    x = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {x}')
    