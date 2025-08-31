import sys
input = sys.stdin.readline
import bisect

c, n = map(int, input().split())
t = [int(input()) for _ in range(c)]
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((b, a))
t.sort()
ab.sort()

cnt = 0
visited = [0]*c
for b, a in ab:
    if len(t) == 0:
        break
    i = bisect.bisect_left(t, a)
    if i < len(t) and t[i] <= b:
        cnt += 1
        t.pop(i)

print(cnt)