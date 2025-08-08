import sys
import heapq
input = sys.stdin.readline

def cal(g, n, x):
    path = [float('inf')]*(n+1)
    path[x] = 0
    h = [(0, x)]

    while h:
        w, v = heapq.heappop(h)
        if w > path[v]:
            continue
        for nv, nw in g[v]:
            if nw + w < path[nv]:
                path[nv] = nw + w
                heapq.heappush(h, (nw+w, nv))
    return path[1:]

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[b].append((a, t))
    graph2[a].append((b, t))

ans = [x+y for x, y in zip(cal(graph, n, x), cal(graph2, n, x))]
print(max(ans))