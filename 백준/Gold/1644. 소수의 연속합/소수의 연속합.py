N = int(input())
P = [1]*(N+1)
i = 2
while i**2 <= N:
    if P[i]:
        for j in range(i*i, N+1, i):
            P[j] = 0
    i += 1
A = [x for x in range(2, N+1) if P[x]]
B = [0]*(len(A)+1)
for i in range(1, len(B)):
    B[i] = B[i-1] + A[i-1]
i, j = 0, 1
ans = 0
while j < len(B):
    tmp = B[j] - B[i]
    if tmp == N:
        ans += 1
        i += 1
    elif tmp > N: i += 1
    else: j += 1
print(ans)