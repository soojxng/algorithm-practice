import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dag = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    dag[u].append(v)
s = int(input())
fan = set(map(int, input().split()))
if 1 in fan:
    print('Yes')
else:
    q = deque([1])
    visited = [0]*(n+1)
    visited[1] = 1
    while q:
        v = q.popleft()
        for nv in dag[v]:
            if visited[nv] == 0 and nv not in fan:
                visited[nv] = 1
                q.append(nv)
    for i in range(1, n+1):
        if visited[i] == 1 and len(dag[i]) == 0:
            print('yes')
            break
    else:
        print('Yes')
            