import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0]*n
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
q = deque()
ans = 0
for i in range(n):
    if indegree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    ans += 1
    for u in graph[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            q.append(u)

print(1 if ans < n else 0)
