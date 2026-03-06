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

for i in range(1, n+1):
    w = int(input())
    edges.append((w, 0, i))

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(i, n):
        edges.append((tmp[j], i, j+1))

edges.sort()

ans = 0
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += w
print(ans)