import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    arr = [[0]*720 for _ in range(42)]
    n = int(input())
    for _ in range(n):
        ch, *tmp = input().rstrip().split()
        a, b, c = map(int, tmp)
        if ch == 'C':
            if b <= c:
                for i in range(b, c):
                    arr[a*2][2*i] = 1
                    arr[a*2][2*i+1] = 1
            else:
                for i in range(c):
                    arr[a*2][2*i] = 1
                    arr[a*2][2*i+1] = 1
                for i in range(b, 360):
                    arr[a*2][2*i] = 1
                    arr[a*2][2*i+1] = 1
            arr[a*2][2*c]
        elif ch == 'S':
            for i in range(a, b):
                arr[i*2][2*c] = 1
                arr[i*2+1][2*c] = 1
            arr[a*2][2*b]

    q = deque([(1, i) for i in range(720) if not arr[1][i]])
    arr[1] = [1]*720
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = 'NO'
    while q:
        x, y = q.popleft()
        if x > 40:
            ans = 'YES'
            break

        for dx, dy in d:
            nx = x + dx
            ny = (y + dy) % 720
            if 0 <= nx <= 41 and not arr[nx][ny]:
                arr[nx][ny] = 1
                q.append((nx, ny))

    print(ans)