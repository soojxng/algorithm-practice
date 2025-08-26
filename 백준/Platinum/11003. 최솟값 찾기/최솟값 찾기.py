import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = deque()
ans = []

for i in range(n):
    while d and a[d[-1]] > a[i]:
        d.pop()
    d.append(i)
    if d[0] <= i - l:
        d.popleft()
    ans.append(a[d[0]])
    
print(*ans)