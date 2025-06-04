import sys
from collections import deque
input = sys.stdin.readline

def bfs(E, R):
    visited[R] = 1
    cnt = 2
    q = deque([R])
    while q:
        x = q.popleft()
        for v in E[x]:
            if visited[v] == 0:
                visited[v] = cnt
                cnt += 1
                q.append(v)
        
N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited[R] = 1
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
for i in range(N+1):
    E[i].sort()
    
bfs(E, R)

for v in visited[1:]:
    print(v)