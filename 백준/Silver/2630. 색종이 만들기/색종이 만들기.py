import sys
input = sys.stdin.readline

def cut(colors, ans, x, y, n):
    tmp = sum(colors[i][j] for i in range(x, x+n) for j in range(y, y+n))
    if tmp == 0:
        ans[0] += 1
    elif tmp == n*n:
        ans[1] += 1
    else:
        if n // 2 != 0:
            cut(colors, ans, x, y, n//2)
            cut(colors, ans, x+(n//2), y, n//2)
            cut(colors, ans, x, y+(n//2), n//2)
            cut(colors, ans, x+(n//2), y+(n//2), n//2)
            
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

cut(colors, ans, 0, 0, N)

print(ans[0])
print(ans[1])