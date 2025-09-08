import heapq

n, t = map(int, input().split())
p = list(map(int, input().split()))
cnt = [0]*n
h = []
for i in range(n):
    heapq.heappush(h, (-p[i], i))

for i in range(1, t+1):
    s, j = heapq.heappop(h)
    cnt[j] += 1
    heapq.heappush(h, (-p[j]+i, j))

print(*cnt)