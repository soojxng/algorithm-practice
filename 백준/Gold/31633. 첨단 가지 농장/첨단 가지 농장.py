import sys
from collections import deque
input = sys.stdin.readline

def cal(a, b):
    graph[a].add(b)
    indegree[b] += 1

n, m = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(n)]

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
ids = [[-1]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if ids[i][j] != -1:
            continue
        q = deque([(i, j)])
        ids[i][j] = cnt
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and ids[nx][ny] == -1 and S[x][y] == S[nx][ny]:
                    ids[nx][ny] = cnt
                    q.append((nx, ny))
        cnt += 1

graph = [set() for _ in range(cnt)]
indegree = [0]*cnt

for i in range(n):
    for j in range(m):
        for dx, dy in ((1, 0), (0, 1)):
            nx, ny = i + dx, j + dy
            if nx < n and ny < m:
                if ids[i][j] == ids[nx][ny]:
                    continue
                elif S[i][j] < S[nx][ny] and ids[nx][ny] not in graph[ids[i][j]]:
                    cal(ids[i][j], ids[nx][ny])
                elif S[i][j] > S[nx][ny] and ids[i][j] not in graph[ids[nx][ny]]:
                    cal(ids[nx][ny], ids[i][j])

q = deque()
ans = [0]*cnt
for i in range(cnt):
    if indegree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    for u in graph[v]:
        if ans[u] < ans[v]+1:
            ans[u] = ans[v]+1
        indegree[u] -= 1
        if indegree[u] == 0:
            q.append(u)

ret = [[ans[ids[i][j]] for j in range(m)] for i in range(n)]
for r in ret:
    print(*r)