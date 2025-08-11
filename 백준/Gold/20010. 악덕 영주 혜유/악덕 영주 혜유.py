import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    for v, d in graph[n]:
        if visited[v] == -1:
            visited[v] = d + visited[n]
            dfs(v)

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

v, e = map(int, input().split())
edges = []
parents = [i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

graph = [[] for _ in range(v)]
ans = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        graph[a].append((b, c))
        graph[b].append((a, c))
        
visited = [-1]*v
visited[0] = 0
dfs(0)
n = visited.index(max(visited))
visited = [-1]*v
visited[n] = 0
dfs(n)
print(ans)
print(max(visited))