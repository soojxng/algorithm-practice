import heapq

N, K = map(int, input().split())
M = 100000
paths = [float('inf')]*(M+1)
paths[N] = 0
h = [(0, N)]
while h:
    w, v = heapq.heappop(h)
    if w > paths[v]:
        continue
    for nv, nw in ((2*v, 0+w), (v-1, 1+w), (v+1, 1+w)):
        if 0 <= nv <= M and paths[nv] > nw:
            paths[nv] = nw
            heapq.heappush(h, (nw, nv))    

print(paths[K])