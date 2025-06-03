import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(E, R):
    global cnt
    cnt += 1
    visited[R] = cnt
    for x in E[R]:
        if visited[x] == 0: dfs(E, x)
        
N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
for i in range(N+1):
    E[i].sort(reverse=1)
    
dfs(E, R)

for v in visited[1:]:
    print(v)