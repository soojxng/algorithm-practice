import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [[0]*M for _ in range(K)]
for i in range(M):
    tmp = list(map(int, input().split()))
    for j in range(K):
        B[j][i] =tmp[j]

C = [[0]*K for _ in range(N)]
for i in range(0, N):
    for j in range(0, K):
        C[i][j] = sum(x*y for x, y in zip(A[i], B[j]))

for c in C:
    print(' '.join(map(str, c)))