import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graphs = [[] for _ in range(n+1)]
costs = [float('inf')]*(n+1)
paths = [0]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graphs[a].append((b, c))
x, y = map(int, input().split())

costs[x] = 0
paths[x] = 0
h = [(0, x)]

while h:
    w, v = heapq.heappop(h)
    if w > costs[v]:
        continue
    for nv, nw in graphs[v]:
        if nw + w < costs[nv]:
            costs[nv] = nw + w
            paths[nv] = v
            heapq.heappush(h, (nw+w, nv))

print(costs[y])
ans = [y]
while ans[-1] != x:
    ans.append(paths[ans[-1]])
print(len(ans))
print(*reversed(ans))