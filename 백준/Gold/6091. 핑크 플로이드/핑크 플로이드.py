import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

n = int(input())
edges = []
parents = [i for i in range(n+1)]

for i in range(1, n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        edges.append((tmp[j], i, i+j+1))

edges.sort()

graph = [[] for _ in range(n+1)]
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        graph[u].append(v)
        graph[v].append(u)
        
for g in graph[1:]:
    print(len(g), *sorted(g))