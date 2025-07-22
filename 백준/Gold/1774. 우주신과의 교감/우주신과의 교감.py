import sys
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

n, m = map(int, input().split())
dots = []
edges = []
prev_edges = []
parents = [i for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(i):
        c, d = dots[j]
        edges.append((((a-c)*(a-c))+((b-d)*(b-d)), i, j))
    dots.append((a, b))
        
edges.sort()

ans = 0

for i in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)
    
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c**0.5
print('{:.2f}'.format(ans))