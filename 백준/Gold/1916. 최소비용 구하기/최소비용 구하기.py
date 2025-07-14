import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graphs = [[] for _ in range(n+1)]
paths = [float('inf')]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graphs[a].append((b, c))
x, y = map(int, input().split())

paths[x] = 0
h = [(0, x)]

while h:
    w, v = heapq.heappop(h)
    if w > paths[v]:
        continue
    for nv, nw in graphs[v]:
        if nw + w < paths[nv]:
            paths[nv] = nw + w
            heapq.heappush(h, (nw+w, nv))

print(paths[y])