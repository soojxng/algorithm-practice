import sys

nums = [0] * (1001)
primes = [[] for _ in range(1001)]
for i in range(2, 1001):
    for j in range(i*2, 1001, i):
        nums[j] = 1

for l in sys.stdin.readlines():
    N, C = map(int, l.split())
    if len(primes[N]) == 0:
        for i in range(1, N+1):
            if nums[i] == 0:
                primes[N].append(i)
    s, e = 0, len(primes[N])
    size = C*2 if e % 2 == 0 else C*2-1
    if size < e:
        s = (e//2) - (size//2)
        e = s + size
    print(f"{N} {C}: {' '.join(map(str, primes[N][s:e]))}")
    print()