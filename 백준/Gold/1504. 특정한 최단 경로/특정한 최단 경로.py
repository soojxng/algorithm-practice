import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())

graphs = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graphs[a].append((b, c))
    graphs[b].append((a, c))

v1, v2 = map(int, input().split())

def cal(V, n):
    paths = [float('inf')]*(V+1)
    paths[n] = 0
    h = [(0, n)]
    while h:
        w, v = heapq.heappop(h)
        if w > paths[v]:
            continue
        for nv, nw in graphs[v]:
            if nw + w < paths[nv]:
                paths[nv] = nw + w
                heapq.heappush(h, (nw+w, nv))
    return paths

p1 = cal(N, 1)
pv1 = cal(N, v1)
pv2 = cal(N, v2)

ans = min(p1[v1] + pv1[v2] + pv2[N], p1[v2] + pv2[v1] + pv1[N])
print(ans if ans != float('inf') else -1)
