import sys
import heapq
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: x[1])
h = []

for p, d in li:
    heapq.heappush(h, p)
    if d < len(h):
        heapq.heappop(h)

print(sum(h))