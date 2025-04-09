import sys
from collections import deque
input = sys.stdin.readline

def dfs(graphs, visited, v, ans_d):
    ans_d.append(v)
    visited[v] = 1
    for n in graphs[v]:
        if visited[n] == 0:
            dfs(graphs, visited, n, ans_d)
    
def bfs(graphs, v, ans_b):
    q = deque([v])
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    
    while q:
        tmp = q.popleft()
        
        for i in graphs[tmp]:
            if visited[i] == 0:
                q.append(i)
                ans_b.append(i)
                visited[i] = 1
        
    
N, M, V = map(int, input().split())
graphs = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
ans_d = []
ans_b = [V]

for m in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
for i in range(1, N+1):
    graphs[i].sort()
  
dfs(graphs, visited, V, ans_d)
bfs(graphs, V, ans_b)
print(' '.join(map(str, ans_d)))
print(' '.join(map(str, ans_b)))