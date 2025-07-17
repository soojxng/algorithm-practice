import sys
input = sys.stdin.readline

W, S = map(int, input().split())
X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(W)]
cut = [0]*X
for _ in range(S):
    tmp = list(map(int, input().split()))
    for i in range(X):
        cut[i] = max(tmp[i], cut[i])
cut = [Y-cut[i] for i in range(X)]
for i in range(W):
    arr[i] = [arr[i][j] if arr[i][j] < cut[j] else cut[j] for j in range(X)]
    print(*arr[i])