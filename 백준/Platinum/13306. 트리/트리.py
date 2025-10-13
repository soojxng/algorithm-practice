import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parents[pb] = pa

n, q = map(int, input().split())

parents = [i for i in range(n+1)]
par = [i for i in range(n+1)]
for i in range(2, n+1):
    a = int(input())
    par[i] = a

tmp = [list(map(int, input().split())) for _ in range(n-1+q)]
tmp.reverse()

ans = []
for t in tmp:
    if not t[0]:
        union(t[1], par[t[1]])
    else:
        ans.append(find(t[1]) == find(t[2]))

for a in reversed(ans):
    print('YES' if a else 'NO')