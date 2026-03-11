import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
for _ in range(n):
    te, tx = map(int, input().split())
    d[te] += 1
    d[tx] -= 1

max_cnt = 0
cnt = 0
ans = [0, 0]
f = 0
for t in sorted(d.keys()):
    cnt += d[t]
    if cnt > max_cnt:
        max_cnt = cnt
        ans[0] = t
        f = 1
    elif cnt < max_cnt and f:
        ans[1] = t
        f = 0

print(max_cnt)
print(*ans)