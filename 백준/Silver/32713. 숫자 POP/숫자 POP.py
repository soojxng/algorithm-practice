import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = [i]
    else:
        d[a[i]].append(i)

L = 0
for inds in d.values():
    l = 0
    for r in range(len(inds)):
        while inds[r] - inds[l] - r + l > k:
            l += 1
        L = max(L, r - l + 1)
print(L)