import sys
from collections import deque
input = sys.stdin.readline

def findI(campus):
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                return (i, j)

def wander(x, y):
    cnt = 0 
    v = [[0]*M for _ in range(N)]
    v[x][y] = 1
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        if campus[x][y] == 'P':
            cnt += 1
            
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and not v[xx][yy] and campus[xx][yy] != 'X':
                v[xx][yy] = 1
                q.append((xx, yy))
                
    return cnt

N, M = map(int, input().split())
campus = [input().strip() for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

I = findI(campus)

cnt = wander(I[0], I[1])
print(cnt if cnt else 'TT')

