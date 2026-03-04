import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

n, m = map(int, input().split())
edges = []
parents = [i for i in range(n+1)]
mw = list(input().rstrip().split())

for _ in range(m):
    u, v, d = map(int, input().split())
    if mw[u-1] != mw[v-1]:
        edges.append((d, u, v))

edges.sort()

ans = 0
cnt = 0
for d, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += d
        cnt += 1
print(ans if cnt == n-1 else -1)