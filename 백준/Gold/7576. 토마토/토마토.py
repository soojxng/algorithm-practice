import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
boxes = [[0]*M for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque()

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            q.append((i, j, 0))
        if tmp[j] != 0:
            boxes[i][j] = tmp[j]
            
while q:
    r, c, cnt = q.popleft()
    for dy, dx in d:
        rr = r + dy
        cc = c + dx
        if 0 <= rr < N and 0 <= cc < M and boxes[rr][cc] == 0:
            boxes[rr][cc] = 1
            q.append((rr, cc, cnt+1))
            
for k in boxes:
    if 0 in k:
        print(-1)
        break
else: print(cnt)