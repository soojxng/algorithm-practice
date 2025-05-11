N, K = map(int, input().split())
temps = list(map(int, input().split()))
m = sum(temps[:K])
tmp = m
for i in range(K, N):
    tmp = tmp - temps[i-K] + temps[i]
    if tmp > m: m = tmp
print(m)