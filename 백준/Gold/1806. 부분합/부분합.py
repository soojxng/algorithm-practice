N, S = map(int, input().split())
A = list(map(int, input().split()))
B = [0]*(N+1)
for i in range(1, N+1):
    B[i] = B[i-1] + A[i-1]
i, j = 0, 1
ans = float('inf')
while j <= N:
    tmp = B[j] - B[i]
    if tmp >= S:
        ans = min(ans, j-i)
        i += 1
    else: j += 1
    if ans == 1:
        break
print(ans if ans != float('inf') else 0)