import sys
input = sys.stdin.readline
import heapq

n = int(input())
h1 = [-int(input())]
print(-h1[0])
h2 = []
for i in range(2, n+1):
    x = int(input())
    if i % 2 == 0:
        heapq.heappush(h2, x)
    else:
        heapq.heappush(h1, -x)
    if -h1[0] > h2[0]:
        heapq.heappush(h1, -heapq.heappop(h2))
        heapq.heappush(h2, -heapq.heappop(h1))
    print(-h1[0])