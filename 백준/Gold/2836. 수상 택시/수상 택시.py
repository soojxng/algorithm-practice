import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        li.append((b, a))

li.sort()
ans = m
c, d = 0, 0
for a, b in li:
    if a > d:
        ans += 2*(d-c)
        c, d = a, b
    else:
        d = max(b, d)
ans += 2*(d-c)

print(ans)