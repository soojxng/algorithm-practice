import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
paths = [float('inf')]*(N+1)
paths[1] = 0
f = 0
for i in range(N):
    for a, b, c in graph:
        if paths[a] != float('inf') and paths[b] > paths[a]+c:
            paths[b] = paths[a] + c
            if i == N-1:
                f = 1
if f:
    print(-1)
else:
    for p in paths[2:]:
        print(-1 if p == float('inf') else p)