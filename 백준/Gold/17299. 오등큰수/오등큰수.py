s = []
n = int(input())
a = list(map(int, input().split()))
ans = [-1] * n
d = dict()
for b in a:
    if b not in d:
        d[b] = 1
    else:
        d[b] += 1

for i in range(n):
    while s and d[a[s[-1]]] < d[a[i]]:
        j = s.pop()
        ans[j] = a[i]
    s.append(i)
print(*ans)