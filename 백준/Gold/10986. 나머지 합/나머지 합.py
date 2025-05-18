N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0]*M

for i in range(1, N+1):
    A[i] = (A[i] + A[i-1]) % M
    B[A[i]] += 1

cnt = B[0]    
for b in B:
    if b > 1:
        cnt += b*(b-1)//2

print(cnt)