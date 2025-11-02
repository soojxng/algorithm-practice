import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(n)]

l, r = 0, 1
LIMIT = 10**(-6)
while r - l >= LIMIT:
    m = (l + r) / 2
    tmp = [p - m * q for p, q in scores]
    tmp.sort(reverse=True)
    if sum(tmp[:k]) >= 0:
        l = m
    else:
        r = m

print(l)