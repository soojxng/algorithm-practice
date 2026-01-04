import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, l, k = map(int, input().split())
    l *= 2520
    graph[a].append((b, l, k))
    graph[b].append((a, l, k))

times = [[float('inf')]*11 for _ in range(n+1)]
times[1][1] = 0
h = [(0, 1, 1)]

while h:
    t, v, a = heapq.heappop(h)

    if t > times[a][v]:
        continue

    for b, l, k in graph[a]:
        for nv in (v-1, v, v+1):
            if nv < 1 or nv > k:
                continue

            nt = t + (l // nv)
            if nt < times[b][nv]:
                times[b][nv] = nt
                heapq.heappush(h, (nt, nv, b))

min_val = min(times[n])
a = min_val // 2520
b = (min_val % 2520)*(10**10) // 2520
if b % 10 >= 5:
    b += 10
b = str(b//10)
print(f"{a}.{'0'*(9-len(b))}{b}")