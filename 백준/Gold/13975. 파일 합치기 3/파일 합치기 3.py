import sys
input = sys.stdin.readline
import heapq

for t in range(int(input())):
    k = int(input())
    h = list(map(int, input().split()))
    heapq.heapify(h)
    ans = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h, a+b)
        ans += a+b
    print(ans)