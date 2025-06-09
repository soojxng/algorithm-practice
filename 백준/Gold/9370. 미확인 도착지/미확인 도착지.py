import sys
import heapq
input = sys.stdin.readline

def cal(n, s):
    paths = [float('inf')]*(n+1)
    paths[s] = 0
    heap = [(0, s)]
    while heap:
        w, v = heapq.heappop(heap)
        if w > paths[v]:
            continue
        for nv, nw in graph[v]:
            if nw + w < paths[nv]:
                paths[nv] = nw+w
                heapq.heappush(heap, (nw+w, nv))
    return paths

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    des = sorted(int(input()) for i in range(t))
    ss = cal(n, s)
    gg = cal(n, g)
    hh = cal(n, h)
    ans = []
    for d in des:
        if ss[d] == float('inf'):
            continue
        if ss[g]+gg[h]+hh[d] == ss[d] or ss[h]+hh[g]+gg[d] == ss[d]:
            ans.append(d)
    print(' '.join(map(str, ans)))
