import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    s = []
    root = -1
    while 1:
        if visited[x][y]:
            root = find(convert(x, y))
            break
        visited[x][y] = 1
        s.append((x, y))
        dx, dy = dir[D[x][y]]
        dx *= L[x][y]
        dy *= L[x][y]
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
        else:
            root = len(size)
            parents.append(root)
            size.append(0)
            break
    for x, y in s:
        union(root, convert(x, y))

def convert(x, y):
    return (x*m) + y

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]
    
def union(pa, b):
    pb = find(b)
    if pa == pb:
        return
    if pa > pb:
        pa, pb = pa, pb
    parents[pb] = pa
    size[pa] += size[pb]

n, m, k = map(int, input().split())
parents = [i for i in range(n*m)]
size = [1]*(n*m)
visited = [[0]*m for _ in range(n)]
D = [list(input().split()) for _ in range(n)]
L = [list(map(int, input().split())) for _ in range(n)]
dir = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)

escape = [size[i] for i in range(n*m, len(size))]
escape.sort(reverse=1)
cycle = set(find(convert(i,j)) for i in range(n) for j in range(m) if find(convert(i, j)) < n*m)
cycle = [size[i] for i in cycle]
cycle.sort(reverse=1)

total = sum(escape)
min_val = total - sum(escape[:k])
max_val = total + sum(cycle[:k])

print(min_val, max_val)