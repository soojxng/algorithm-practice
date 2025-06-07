import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())


graphs = [[] for _ in range(V+1)]
paths = [float('inf')]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graphs[u].append((w, v))

paths[K] = 0
h = [(0, K)]

while h:
    w, v = heapq.heappop(h)
    if w > paths[v]:
        continue
    for nw, nv in graphs[v]:
        if nw + w < paths[nv]:
            paths[nv] = nw + w
            heapq.heappush(h, (nw+w, nv))

for p in paths[1:]:
    print(p if p != float('inf') else 'INF')