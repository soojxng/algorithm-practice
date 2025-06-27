import sys
from collections import deque
#input = sys.stdin.readline

def right(n, d):
    tmp = [2, 6]
    while 1:
        if n >= 3:
            break
        if wheels[n][tmp[0]] != wheels[n+1][tmp[1]]:
            f[n+1] = d
            d = -d
            n += 1
        else:
            break
        
def left(n, d):
    tmp = [6, 2]
    while 1:
        if n-1 < 0:
            break
        if wheels[n][tmp[0]] != wheels[n-1][tmp[1]]:
            f[n-1] = d
            d = -d
            n -= 1
        else:
            break        

wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    f = [0, 0, 0, 0]
    f[n-1] = d 
    left(n-1, -d)
    right(n-1, -d)
    for i in range(4):
        if f[i] != 0:
            wheels[i].rotate(f[i])

ans = 0
tmp = [1, 2, 4, 8]
for i in range(4):
    if wheels[i][0]:
        ans += tmp[i]
print(ans)