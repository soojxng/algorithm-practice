import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, pv):
    for nv, nd in tree[v]:
        if nv != pv:
            parents[0][nv] = v
            depth[nv] = depth[v] + 1
            dist[nv] = dist[v] + nd
            dfs(nv, v)

def find_lca(a, b):
    if depth[a] < depth[b]: a, b = b, a
    tmp = depth[a] - depth[b]
    for k in range(LOG):
        if tmp & (1<<k):
            a = parents[k][a]
    if a == b:
        return a
    for k in range(LOG-1, -1, -1):
        pa, pb = parents[k][a], parents[k][b]
        if pa != pb:
            a = pa
            b = pb
    return parents[0][a]

def find_LOG():
    LOG = 1
    tmp = 2
    while tmp < n:
        LOG += 1
        tmp *= 2
    return LOG

n = int(input())
tree = [[] for _ in range(n+1)]
LOG = find_LOG()
parents = [[0]*(n+1) for _ in range(LOG)]
depth = [0]*(n+1)
dist = [0]*(n+1)

for i in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

dfs(1, 0)
for k in range(1, LOG):
    for v in range(1, n+1):
        parents[k][v] = parents[k-1][parents[k-1][v]]

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    lca = find_lca(a, b)
    print(dist[a] + dist[b] - 2*dist[lca])