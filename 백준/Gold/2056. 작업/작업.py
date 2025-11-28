import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tasks = [[] for _ in range(n+1)]
times = [0]*(n+1)
indegree = [0]*(n+1)
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    for j in range(2, len(tmp)):
        tasks[tmp[j]].append(i)
        indegree[i] += 1

q = deque()
ans = [0]*(n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = times[i]
        
while q:
    v = q.popleft()
    for nv in tasks[v]:
        indegree[nv] -= 1
        ans[nv] = max(ans[nv], ans[v] + times[nv])
        if indegree[nv] == 0:
            q.append(nv)
            
print(max(ans))