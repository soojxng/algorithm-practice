import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
trees = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)
    
q = deque([1])
ans[1] = -1
while q:
    i = q.popleft()
    for j in trees[i]:
        if ans[j] == 0:
            ans[j] = i
            q.append(j)
            
for k in range(2, n+1):
    print(ans[k])