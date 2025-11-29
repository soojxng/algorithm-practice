import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
classes = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    classes[a].append(b)
    indegree[b] += 1

q = deque()
ans = [0]*(n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = 1
        
while q:
    v = q.popleft()
    for nv in classes[v]:
        indegree[nv] -= 1
        ans[nv] = ans[v] + 1
        if indegree[nv] == 0:
            q.append(nv)
            
print(*ans[1:])