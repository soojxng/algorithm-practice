import sys
input = sys.stdin.readline
from collections import deque

n, m, c, d = map(int, input().split())
b = list(map(int, input().split()))

dp = [m - abs(b[0] - i) for i in range(m+1)]

for x in range(1, n):
    tmp = [0]*(m+1)

    for i in range(1, c+1):
        deq = deque()

        for j in range(i, min(m+1, d+1), c):
            while deq and dp[deq[-1]] <= dp[j]:
                deq.pop()
            deq.append(j)
            
        for j in range(i, m+1, c):
            while deq and deq[0] < j-d:
                deq.popleft()
            while deq and j+d <= m and dp[deq[-1]] <= dp[j+d]:
                deq.pop()
            if j+d <= m: deq.append(j+d)
            tmp[j] = dp[deq[0]] + (m-abs(b[x]-j))

    dp = tmp[::]

print(max(dp))