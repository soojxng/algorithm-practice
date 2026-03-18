import sys
from collections import deque
input = sys.stdin.readline

n, a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    if tmp[0] > 0:
        graph[i].append((0, tmp[1]))
        if tmp[0] > 1:
            for j in range(2, tmp[0]+1):
                graph[i].append((1, tmp[j]))

dist = [float('inf')]*(n+1)
q = deque([a])
dist[a] = 0
while q:
    v = q.popleft()
    if v == b:
        continue
    for nw, u in graph[v]:
        if dist[v]+nw < dist[u]:
            dist[u] = dist[v]+nw
            if nw == 0:
                q.appendleft(u)
            else:
                q.append(u)

print(dist[b] if dist[b] != float('inf') else -1)