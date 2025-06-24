import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(n):
    for v, d in trees[n]:
        if visited[v] == -1:
            visited[v] = d + visited[n]
            dfs(v)

N = int(input())
trees = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
visited[1] = 0
for _ in range(N-1):
    a, b, c = list(map(int, input().split()))
    trees[a].append((b, c))
    trees[b].append((a, c))

dfs(1)
n = visited.index(max(visited))
visited = [-1]*(N+1)
visited[n] = 0
dfs(n)

print(max(visited))