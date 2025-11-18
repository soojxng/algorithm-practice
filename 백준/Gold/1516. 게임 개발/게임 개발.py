import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
buildings = [[] for _ in range(n+1)]
times = [0]*(n+1)
indegree = [0]*(n+1)
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    j = 1
    while tmp[j] != -1:
        buildings[tmp[j]].append(i)
        indegree[i] += 1
        j += 1 

q = deque()
ans = [0]*(n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = times[i]
        
while q:
    v = q.popleft()
    for nv in buildings[v]:
        indegree[nv] -= 1
        ans[nv] = max(ans[nv], ans[v] + times[nv])
        if indegree[nv] == 0:
            q.append(nv)
            
for i in range(1, n+1):
    print(ans[i])