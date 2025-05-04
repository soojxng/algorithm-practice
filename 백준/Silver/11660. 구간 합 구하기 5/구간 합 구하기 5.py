import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        a = arr[i-1][j] if i-1 >= 0 else 0
        b = arr[i][j-1] if j-1 >= 0 else 0
        c = arr[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
        arr[i][j] = arr[i][j] + a + b - c
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    a = arr[x1-2][y2-1] if x1-2 >= 0 else 0
    b = arr[x2-1][y1-2] if y1-2 >= 0 else 0
    c = arr[x1-2][y1-2] if x1-2 >= 0 and y1-2 >= 0 else 0
    print(arr[x2-1][y2-1] - a - b + c)
    