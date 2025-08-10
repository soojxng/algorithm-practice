import sys
from collections import deque
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    dp = [0]*(n+1)
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            indegree[i] = -1
            q.append(i)
    
    while q:
        v = q.popleft()
        dp[v] += d[v-1]
        if v == w:
            print(dp[w])
            break
        for nv in graph[v]:
            dp[nv] = max(dp[nv], dp[v])
            indegree[nv] -= 1
            if indegree[nv] == 0:
                indegree[nv] = -1
                q.append(nv)