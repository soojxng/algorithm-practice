import sys
import heapq
input = sys.stdin.readline

n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]
li.sort()
h = []
ans = 0
for i in range(n-1, -1, -1):
    while li and li[-1][0] > i:
        d, x = li.pop()
        heapq.heappush(h, -x)
    if h:
        ans -= heapq.heappop(h)
print(ans)