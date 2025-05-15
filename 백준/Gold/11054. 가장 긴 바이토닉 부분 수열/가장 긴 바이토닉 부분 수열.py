N = int(input())
A = list(map(int, input().split()))
B = [1 for _ in range(N)]
C = [0 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            B[i] = max(B[i], B[j]+1)

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            C[i] = max(C[i], C[j]+1)
   
print(max(b+c for b, c in zip(B, C)))