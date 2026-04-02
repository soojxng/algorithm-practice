import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a0, b0 = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        f, m = map(int, input().split())
        if f:
            graph[i].append((f, 0))
        if m:
            graph[i].append((m, 1))

    ans = -1
    visited = [float('inf')]*(n+1)
    visited[a0] = 0
    q = deque([(a0, 0)])
    while q:
        v, cnt = q.popleft()
        if cnt > visited[v]:
            continue
        if v == b0:
            ans = cnt
            break
        for nv, f in graph[v]:
            ncnt = cnt + (f if nv != b0 else 0)
            if visited[nv] > ncnt:
                if cnt == ncnt:
                    q.appendleft((nv, ncnt))
                else:
                    q.append((nv, ncnt))
                visited[nv] = ncnt
    print(ans if ans > -1 else "no ancestor")