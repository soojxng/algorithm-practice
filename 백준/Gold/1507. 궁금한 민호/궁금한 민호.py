import sys
input = sys.stdin.readline
 
n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
checked = [[1]*n for _ in range(n)]
f = 1

for i in range(n):
    if not f:
        break
    for j in range(i+1, n):
        if not f:
            break
        for k in range(n):
            if i == k or j == k:
                continue

            if dist[i][j] > dist[i][k] + dist[k][j]:
                f = 0
                break
            elif dist[i][j] == dist[i][k] + dist[k][j]:
                checked[i][j] = 0

if f:
    tot = 0
    for i in range(n):
        for j in range(i+1, n):
            if checked[i][j]:
                tot += dist[i][j]

    print(tot)
else:
    print(-1)