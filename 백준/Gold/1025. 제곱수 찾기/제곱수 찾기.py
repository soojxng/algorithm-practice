import sys
input = sys.stdin.readline

i = 0
s = set()
while 1:
    x = i*i
    if x >= 10**9:
        break
    s.add(x)
    i += 1

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        for k in range(-n, n):
            for l in range(-m, m):
                if k == l == 0:
                    continue
                tmp = ''
                x, y = i, j
                while 0 <= x < n and 0 <= y < m:
                    tmp += board[x][y]
                    val = int(tmp)
                    if val in s:
                        ans = max(ans, val)
                    x += k
                    y += l

print(ans)