N = int(input())
A = sorted([list(map(int, input().split())) for _ in range(N)])
B = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j][1] < A[i][1]:
            B[i] = max(B[i], B[j]+1)
   
print(N - max(B))