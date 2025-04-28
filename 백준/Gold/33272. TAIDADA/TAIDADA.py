N, M, K = map(int, input().split())
A = set()
i = 1

while len(A) < N and i <= M:
    if i ^ K not in A:
        A.add(i)
    i += 1
    
print(' '.join(map(str, sorted(A))) if len(A) == N else -1)