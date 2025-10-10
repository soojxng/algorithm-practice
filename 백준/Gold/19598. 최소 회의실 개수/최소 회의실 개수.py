import sys
input = sys.stdin.readline
import heapq

n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort()

h = []
ans = 0
for s, e in meeting:
    while h and h[0] <= s:
        heapq.heappop(h)
    heapq.heappush(h, e)
    ans = max(ans, len(h))

print(ans)