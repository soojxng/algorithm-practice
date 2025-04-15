import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
s = set(i for i in range(1, N+1))
q = deque()
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)
    
while s:
    q.append(s.pop())
    while q:
        for i in graphs[q.popleft()]:
            if i in s:
                q.append(i)
                s.remove(i)
    ans += 1
    
print(ans)