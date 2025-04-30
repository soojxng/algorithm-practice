from collections import deque

A, B = map(int, input().split())
q = deque([(A, 1)])
s = set([A])

while q:
    A, cnt = q.popleft()
    if A == B:
        print(cnt)
        break
    for i in [A*2, A*10+1]:
        if i <= B and i not in s:
            s.add(i)
            q.append((i, cnt+1))
else: print(-1)