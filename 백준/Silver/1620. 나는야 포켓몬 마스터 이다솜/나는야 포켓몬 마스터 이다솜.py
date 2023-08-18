import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d =dict()
for i in range(1, n + 1, 1):
    v = input().rstrip()
    d[i] = v
    d[v] = i
for _ in range(m):
    x = input().rstrip()
    if str.isdigit(x):
        print(d[int(x)])
    else:
        print(d[x])