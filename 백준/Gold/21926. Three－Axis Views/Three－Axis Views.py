import sys
input = sys.stdin.readline

def check(arr1, arr2):
    for i in range(n):
        if arr1[i] != ''.join(arr2[i]):
            return 0
    return 1

n = int(input())
zy = [input().rstrip() for _ in range(n)][::-1]
xz = [input().rstrip() for _ in range(n)][::-1]
yx = [input().rstrip() for _ in range(n)][::-1]
xyz = [[[1 if zy[z][y] == xz[x][z] == yx[y][x] == '1' else 0 for z in range(n)] for y in range(n)] for x in range(n)]

zy2 = [['0']*n for _ in range(n)]
xz2 = [['0']*n for _ in range(n)]
yx2 = [['0']*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        for z in range(n):
            if xyz[x][y][z]:
                zy2[z][y] = '1'
                xz2[x][z] = '1'
                yx2[y][x] = '1'

print("Yes" if check(zy, zy2) and check(xz, xz2) and check(yx, yx2) else "No")