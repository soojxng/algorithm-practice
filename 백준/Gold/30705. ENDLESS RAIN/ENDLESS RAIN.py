import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, input().split())
cnt = 0
parent = [i for i in range(n+2)]

f = 0
for i in range(m):
    a, b = map(int, input().split())
    f += 1

    x = find(a)
    while x < b and x <= n:
        if f == 0:
            cnt += 1
        else:
            f -= 1
        
        nx = find(x+1)
        parent[x] = nx
        x = nx

print(cnt)