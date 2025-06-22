import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(n):
    for v, d in trees[n]:
        if visited[v] == -1:
            visited[v] = d + visited[n]
            dfs(v)

V = int(input())
trees = [[] for _ in range(V+1)]
visited = [-1]*(V+1)
visited[1] = 0
for _ in range(1, V+1):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        trees[tmp[0]].append((tmp[i], tmp[i+1]))

dfs(1)
n = visited.index(max(visited))
visited = [-1]*(V+1)
visited[n] = 0
dfs(n)

print(max(visited))