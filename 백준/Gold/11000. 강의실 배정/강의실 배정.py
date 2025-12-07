import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    classes.append(tuple(map(int, input().split())))

classes.sort()
cnt = 0
h = []
for s, t in classes:
    if h and h[0] <= s:
        heapq.heappop(h)
    heapq.heappush(h, t)
    cnt = max(cnt, len(h))

print(cnt)