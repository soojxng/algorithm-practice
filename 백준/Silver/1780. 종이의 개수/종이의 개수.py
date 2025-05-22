import sys
input = sys.stdin.readline

def cut(colors, ans, x, y, n):
    tmp = colors[x][y]
    f = 1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if colors[i][j] != tmp:
                f = 0
                break
    if f:
        ans[tmp+1] += 1    
    else:
        for i in range(x, x+n, n//3):
            for j in range(y, y+n, n//3):
                cut(colors, ans, i, j, n//3)
                    
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]

cut(colors, ans, 0, 0, N)

for a in ans:
    print(a)