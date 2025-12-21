import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    w = input().rstrip()
    size = len(w)
    x = 10**(size-1)
    for i in range(size):
        if w[i] not in d:
            d[w[i]] = x
        else:
            d[w[i]] += x
        x //= 10

results = sorted(d.values(), reverse=1)
ans = 0
x = 9
for r in results:
    ans += r*x
    x -= 1
print(ans)