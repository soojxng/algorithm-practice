import sys
from collections import deque
input = sys.stdin.readline
 
N, M = map(int, input().split()) 
board = [i for i in range(101)]
for _ in range(N+M):
    a, b = map(int, input().split())
    board[a] = b
    
q = deque([(1, 0)])
while q:
    x, cnt = q.popleft()
    if x == 100:
        print(cnt)
        break
    for d in range(1, 7):
        if x+d <= 100 and board[x+d]:
            q.append((board[x+d], cnt+1))
            board[x+d] = 0
    