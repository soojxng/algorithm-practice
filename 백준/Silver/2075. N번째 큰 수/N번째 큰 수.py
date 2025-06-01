import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)

for _ in range(N-1):
    for x in map(int, input().split()):
        heapq.heappush(h, x)
        heapq.heappop(h)
print(heapq.heappop(h))