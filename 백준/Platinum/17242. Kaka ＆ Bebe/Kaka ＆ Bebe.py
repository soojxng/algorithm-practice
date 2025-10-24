import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

visited = [dict() for _ in range(n)]
h = [(0, 0, 0, 0)]

while h:
    w, k, b, v = heapq.heappop(h)
    
    if (k, b) in visited[v]:
        continue

    visited[v][(k, b)] = w

    for nv, nk, nb in graph[v]:
        nk += k
        nb += b
        if nk >= 1000 or nb >= 1000:
            continue
        nw = nk * nb

        if (nk, nb) in visited[nv]:
            continue
        
        tmp = []
        f = 1
        for pk, pb in visited[nv].keys():
            if pk <= nk and pb <= nb:
                f = 0
                break
            elif nk <= pk and nb <= pb:
                tmp.append((pk, pb))
        if f:
            for x in tmp:
                del visited[nv][x]
            heapq.heappush(h, (nw, nk, nb, nv))

print(min(visited[n-1].values()) if visited[n-1] else -1)