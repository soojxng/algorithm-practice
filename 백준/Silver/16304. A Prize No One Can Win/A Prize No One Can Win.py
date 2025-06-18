N, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans = 1
for i in range(N-1, 0, -1):
    if A[i] + A[i-1] <= X:
        ans = i+1
        break
print(ans)