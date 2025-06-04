import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    connections = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)
    
    flag = 1
    visited = [0]*(V+1)
    for i in range(1, V+1):
        if flag == 0: break
        if visited[i] == 0:
            q = deque([(i, 1)])
            visited[i] = 1
            while q:
                x, f = q.popleft()
                for v in connections[x]:
                    if visited[v] == f:
                        flag = 0
                        break
                    elif visited[v] == 0:
                        visited[v] = -f
                        q.append((v, -f))
    print('YES' if flag else 'NO')