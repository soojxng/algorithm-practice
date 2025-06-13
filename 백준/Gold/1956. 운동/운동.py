import sys
input = sys.stdin.readline

V, E = map(int, input().split())
dist = [[float('inf')]*V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        if i == k: continue
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = min(dist[x][x] for x in range(V))
print(ans if ans != float('inf') else -1)