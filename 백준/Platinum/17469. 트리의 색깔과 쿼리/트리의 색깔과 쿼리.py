import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if parents2[a] != a:
        parents2[a] = find(parents2[a])
    return parents2[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if len(colors[pa]) <= len(colors[pb]):
        pa, pb = pb, pa
    parents2[pb] = pa
    colors[pa] |= colors[pb]

n, q = map(int, input().split())
parents = [i for i in range(n+1)]
parents2 = [i for i in range(n+1)]
colors = [set() for _ in range(n+1)]
for i in range(2, n+1):
    parents[i] = int(input())
for i in range(1, n+1):
    colors[i].add(int(input()))
queries = [tuple(map(int, input().split())) for _ in range(n+q-1)]
results = []
for i in range(n+q-2, -1, -1):
    x, a = queries[i]
    if x == 1:
        union(parents[a], a)
    elif x == 2:
        pa = find(a)
        results.append(len(colors[pa]))

for x in reversed(results):
    print(x)