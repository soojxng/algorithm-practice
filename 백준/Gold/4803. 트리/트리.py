import sys
input = sys.stdin.readline

def is_cycle(p, x):
    for v in graph[x]:
        if visited[v] == 0:
            visited[v] = 1
        elif v == p:
            continue
        elif v != p:
            return 1
        if is_cycle(x, v):
            return 1
    return 0
   
case = 0
while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    case += 1
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    tree = []
    cnt = 0
    for v in range(1, n+1):
        if visited[v] == 0:
            visited[v] = 1
            if not is_cycle(0, v):
                cnt += 1
                
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')