N = int(input())
A = list(map(int, input().split()))
B = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            B[i] = max(B[i], B[j]+1)
            
print(max(B))