import sys
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)
    parents[pb] = pa

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

n = int(input())
m = int(input())
parents = [i for i in range(n+1)]
enemies = [-1] * (n+1)
for _ in range(m):
    x, p, q = input().rstrip().split()
    p, q = int(p), int(q)
    if x == 'F':
        union(p, q)
    elif x == 'E':
        if enemies[p] > 0:
            union(q, enemies[p])
        else:
            enemies[p] = q
        if enemies[q] > 0:
            union(p, enemies[q])
        else:
            enemies[q] = p

visited = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    x = find(i)
    if visited[x] == 0:
        visited[x] = 1
        ans += 1

print(ans)