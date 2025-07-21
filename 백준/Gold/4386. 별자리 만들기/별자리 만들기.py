import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

n = int(input())
dots = []
edges = []
parents = [i for i in range(n)]

for i in range(n):
    a, b = map(float, input().split())
    for j in range(i):
        c, d = dots[j]
        edges.append((((a-c)*(a-c))+((b-d)*(b-d)), i, j))
    dots.append((a, b))
        
edges.sort()

ans = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c**0.5
print(ans)