import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
costs = [[float('inf')]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a-1][b-1] = min(costs[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if i==j or j==k:
                continue
            costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])
for r in costs:
    for c in r:
        print(0 if c == float('inf') else c, end=' ')
    print()