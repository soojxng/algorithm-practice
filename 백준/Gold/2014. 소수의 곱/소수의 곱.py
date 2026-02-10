import sys
import heapq
input = sys.stdin.readline

k, n = map(int, input().split())
p = list(map(int, input().split()))

h = p[::]
heapq.heapify(h)

for _ in range(n):
    a = heapq.heappop(h)
    for x in p:
        heapq.heappush(h, a*x)
        if a % x == 0:
            break
print(a)