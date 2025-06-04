import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1
    
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        indegree[i] = -1
        q.append(i)
while q:
    v = q.popleft()
    print(v, end=' ')
    for a in arr[v]:
        indegree[a] -= 1
        if indegree[a] == 0:
            indegree[a] = -1
            q.append(a)