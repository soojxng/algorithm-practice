N = int(input())
A = list(map(int, input().split()))
B = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            B[i] = max(B[i], B[j]+1)
            
i = max(B)
ans = [float('inf')]
for j in range(B.index(max(B)), -1, -1):
    if i == 0:
        break
    if i == B[j] and A[j] < ans[-1]:
        ans.append(A[j])
        i -= 1
print(len(ans)-1)
print(*reversed(ans[1:]))