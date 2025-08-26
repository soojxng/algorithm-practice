import sys
input = sys.stdin.readline
from collections import deque

n, d = map(int, input().split())
dp = list(map(int, input().split()))
deq = deque()

for i in range(n):
    if deq and deq[0] < i - d:
        deq.popleft()
    dp[i] += max(0, dp[deq[0]] if deq else 0)
    while deq and dp[deq[-1]] < dp[i]:
        deq.pop()
    deq.append(i)
    
print(max(dp))