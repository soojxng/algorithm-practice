import sys
input = sys.stdin.readline

n, m = map(int, input().split())
b = list(map(int, input().split()))
a = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x] = y

lr = []
tmp = 1
for i in range(1, n+1):
    if b[i-1] == 1:
        lr.append((tmp, i))
        tmp = i+1

f = 1
for l, r in lr:
    if not f:
        break
    s = set()
    for i in range(l, r+1):
        if a[i] and a[i] < l or a[i] > r:
            f = 0
            break
        if a[i]:
            s.add(a[i])
    x = r
    for i in range(l, r+1):
        if a[i]:
            continue
        while x in s:
            x -= 1
        a[i] = x
        x -= 1

max_val = 0
for i in range(1, n+1):
    max_val = max(max_val, a[i])
    if not b[i-1] and max_val <= i:
        f = 0
        break

print((' '.join(map(str, a[1:])) if f else -1))