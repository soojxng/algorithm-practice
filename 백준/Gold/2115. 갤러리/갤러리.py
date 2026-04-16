import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
gallery = [list(input().rstrip()) for _ in range(m)]

cnt = 0
tmp = 0
f = 0
for i in range(1, m):
    for j in range(n):
        if gallery[i-1][j] == 'X' and gallery[i][j] == '.':
            if not f:
                f = 1
            tmp += 1
        elif f:
            cnt += tmp // 2
            tmp = 0
            f = 0
    if f:
        cnt += tmp // 2
        tmp = 0
        f = 0

for i in range(m-1):
    for j in range(n):
        if gallery[i+1][j] == 'X' and gallery[i][j] == '.':
            if not f:
                f = 1
            tmp += 1
        elif f:
            cnt += tmp // 2
            tmp = 0
            f = 0
    if f:
        cnt += tmp // 2
        tmp = 0
        f = 0

for j in range(1, n):
    for i in range(m):
        if gallery[i][j-1] == 'X' and gallery[i][j] == '.':
            if not f:
                f = 1
            tmp += 1
        elif f:
            cnt += tmp // 2
            tmp = 0
            f = 0
    if f:
        cnt += tmp // 2
        tmp = 0
        f = 0

for j in range(n-1):
    for i in range(m):
        if gallery[i][j+1] == 'X' and gallery[i][j] == '.':
            if not f:
                f = 1
            tmp += 1
        elif f:
            cnt += tmp // 2
            tmp = 0
            f = 0
    if f:
        cnt += tmp // 2
        tmp = 0
        f = 0

print(cnt)