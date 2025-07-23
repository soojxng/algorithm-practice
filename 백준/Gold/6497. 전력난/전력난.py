import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    parents[find(a)] = find(b)

while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    parents = [i for i in range(m)]
    total = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        total += z
        edges.append((z, x, y))
        
    edges.sort()
    
    for z, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            total -= z
    print(total)