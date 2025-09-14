import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

total = sum(a)
dp = [0]*(n+2)

d = deque([0])

for i in range(1, n+2):
    while d and d[0] < i-k-1:
        d.popleft()
    dp[i] = dp[d[0]] + (a[i-1] if i < n+1 else 0)
    while d and dp[d[-1]] >= dp[i]:
        d.pop()
    d.append(i)

print(total - dp[-1])