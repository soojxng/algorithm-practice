import sys
input = sys.stdin.readline
import heapq

n = int(input())
ho = []
for _ in range(n):
    a, b = map(int, input().split())
    ho.append([max(a, b), min(a, b)])
d = int(input())
hp = []
ho.sort()
cnt = 0

for b, a in ho:
    if b - a > d:
        continue
    while hp and b - hp[0] > d:
        cnt = max(cnt, len(hp))
        heapq.heappop(hp)
    heapq.heappush(hp, a)

cnt = max(cnt, len(hp))
print(cnt)