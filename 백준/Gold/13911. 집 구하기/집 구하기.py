import sys
import heapq
input = sys.stdin.readline

def cal(v, x):
    dist = [float('inf')]*(V+3)
    dist[v] = 0
    h = [(0, v)]

    while h:
        w, u = heapq.heappop(h)
        if w > dist[u]:
            continue
        for nu, nw in graph[u]:
            if nw + w < min(dist[nu], x):
                dist[nu] = nw + w
                heapq.heappush(h, (nw+w, nu))
    
    return dist

V, E = map(int, input().split())
graph = [[] for _ in range(V+3)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

m, x = map(int, input().split())
mcd = set(map(int, input().split()))
for a in mcd:
    graph[V+1].append((a, 0))

s, y = map(int, input().split())
sta = set(map(int, input().split()))
for a in sta:
    graph[V+2].append((a, 0))

dist = [cal(V+1, x+1), cal(V+2, y+1)]
ans = float('inf')
for v in range(1, V+1):
    if v in mcd or v in sta:
        continue
    ans = min(ans, dist[0][v] + dist[1][v])

print(ans if ans < float('inf') else -1)