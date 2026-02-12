import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    s = []
    tmp = list(range(1, n+1))
    for i in range(n-1, -1, -1):
        if r[i] >= len(tmp):
            break
        x = tmp.pop(r[i])
        s.append(x)
    if len(s) == n:
        print(*s[::-1])
    else:
        print('IMPOSSIBLE')