import sys
input = sys.stdin.readline
from collections import deque

n, k = input().rstrip().split()
k = int(k)

visited = set()
visited.add((n, 0))
q = deque()
q.append((n, 0))
ans = -1

while q:
    s, cnt = q.popleft()
    if cnt == k:
        ans = max(ans, int(s))
        continue
    
    s = list(s)
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if i == 0 and s[j] == '0':
                continue
            s[i], s[j] = s[j], s[i]
            tmp = ''.join(s)
            if (tmp, cnt+1) not in visited:
                visited.add((tmp, cnt+1))
                q.append((tmp, cnt+1))
            s[i], s[j] = s[j], s[i]

print(ans)