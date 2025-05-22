import sys
input = sys.stdin.readline

def cut(images, ans, x, y, n):
    tmp = images[x][y]
    f = 1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if images[i][j] != tmp:
                f = 0
                break
    if f:
        ans.append(tmp)    
    else:
        ans.append('(')
        for i in range(x, x+n, n//2):
            for j in range(y, y+n, n//2):
                cut(images, ans, i, j, n//2)
        ans.append(')')
                    
N = int(input())
images = [list(input().strip()) for _ in range(N)]
ans = []
cut(images, ans, 0, 0, N)
print(''.join(ans))