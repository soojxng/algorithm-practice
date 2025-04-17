import sys
input = sys.stdin.readline

N, M = map(int, input().split())

friends = [[0 if i == j else float('inf') for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1
    
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            friends[j][k] = min(friends[j][k], friends[j][i] + friends[i][k])
   
ans = 0
m = float('inf')

for i in range(1, N+1):
    tmp = sum(friends[i][1:])
    if tmp < m:
        m = tmp
        ans = i
print(ans)