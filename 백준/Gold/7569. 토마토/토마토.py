import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[[0]*M for _ in range(N)] for __ in range(H)]
d = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
q = deque()

for h in range(H):
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j] == 1:
                q.append((h, i, j, 0))
            if tmp[j] != 0:
                boxes[h][i][j] = tmp[j]
            
while q:
    h, r, c, cnt = q.popleft()
    for dh, dy, dx in d:
        hh = h + dh
        rr = r + dy
        cc = c + dx
        if 0 <= rr < N and 0 <= cc < M and 0 <= hh < H and boxes[hh][rr][cc] == 0:
            boxes[hh][rr][cc] = 1
            q.append((hh, rr, cc, cnt+1))
     
flag = 1
for l in boxes:
    for k in l:
        if 0 in k:
            flag = 0
            break
print(cnt if flag else -1)