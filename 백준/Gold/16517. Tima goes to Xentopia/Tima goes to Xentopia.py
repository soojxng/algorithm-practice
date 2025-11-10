import sys
input = sys.stdin.readline
import heapq

n, m, k1, k2 = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, x, c = map(int, input().split())
    graph[u].append((v, x, c))
    graph[v].append((u, x, c))

s, t = map(int, input().split())

dist = [[[float('inf')]*(k2+1) for _ in range(k1+1)] for _ in range(n+1)]
h = []
dist[s][0][0] = 0
heapq.heappush(h, (0, s, 0, 0))

while h:
    x, v, r, b = heapq.heappop(h)
    if dist[v][r][b] < x:
        continue

    for nv, nx, nc in graph[v]:
        nr, nb = r, b
        if nc == 1:
            nr += 1
        elif nc == 2:
            nb += 1

        if nr <= k1 and nb <= k2 and dist[nv][nr][nb] > x+nx:
            dist[nv][nr][nb] = x+nx
            heapq.heappush(h, (x+nx, nv, nr, nb))

print(dist[t][k1][k2] if dist[t][k1][k2] != float('inf') else -1)        