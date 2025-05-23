N, K = map(int, input().split())
MOD = 10**9+7
fac = 1
inv = []

for i in range(1, N+1):
    fac = fac * i % MOD
    if i == K:
        inv.append(pow(fac, MOD-2, MOD))
    if i == N-K:
        inv.append(pow(fac, MOD-2, MOD))
    
print(1 if (K == N or K == 0) else fac * inv[0] % MOD * inv[1] % MOD)
