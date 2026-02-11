import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
k = int(input())

visited = [0]*n
ans = 0

for i in range(n):
    if visited[i]:
        continue
    visited[i] = 1

    cnt = 0
    for x in board[i]:
        if x == '0':
            cnt += 1
    
    tmp = 0
    if cnt <= k and (cnt + k) % 2 == 0:
        for j in range(n):
            if board[i] == board[j]:
                visited[j] = 1
                tmp += 1
    ans = max(ans, tmp)

print(ans)