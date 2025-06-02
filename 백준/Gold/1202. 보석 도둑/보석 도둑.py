import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
h = []
jewels = sorted([list((map(int, input().split()))) for _ in range(N)])
bags = sorted(list(int(input()) for _ in range(K)))
i = 0
cnt = 0
for b in bags:
    while i < N and jewels[i][0] <= b:
        heapq.heappush(h, -jewels[i][1])
        i += 1
    if h:
        cnt += -heapq.heappop(h)
print(cnt)