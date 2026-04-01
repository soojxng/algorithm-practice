import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
p = tuple(map(int, input().split()))
asc = tuple(range(1, n+1))

q = deque([(p, 0)])
s = set()
s.add(p)
ans = -1
while q:
    tmp, cnt = q.popleft()
    if tmp == asc:
        ans = cnt
        break

    for i in range(n-k+1):
        ntmp = list(tmp)
        ntmp[i:i+k] = reversed(ntmp[i:i+k])
        ntmp = tuple(ntmp)
        if ntmp not in s:
            s.add(ntmp)
            q.append((ntmp, cnt+1))
print(ans)