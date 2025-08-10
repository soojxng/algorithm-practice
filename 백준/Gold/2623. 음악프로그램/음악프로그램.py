import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(2, len(tmp)):
        graph[tmp[i-1]].append(tmp[i])
        indegree[tmp[i]] += 1

q = deque()
ans = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans.append(i)
while q:
    v = q.popleft()
    for nv in graph[v]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            ans.append(nv)
            q.append(nv)
            
if len(ans) != n:
    print(0)
else:
    for a in ans:
        print(a)