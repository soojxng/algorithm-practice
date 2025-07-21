import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

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

ans = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)