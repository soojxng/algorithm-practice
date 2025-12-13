import sys
input = sys.stdin.readline

def bt(v, cnt):
    ret = 0
    if cnt == 5:
        return 1
    
    for u in graph[v]:
        if not visited[u]:
            visited[u] = 1
            ret = bt(u, cnt+1)
            visited[u] = 0
        if ret:
            break

    return ret

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*n
for v in range(n):
    visited[v] = 1
    if bt(v, 1):
        print(1)
        break
    visited[v] = 0
else:
    print(0)