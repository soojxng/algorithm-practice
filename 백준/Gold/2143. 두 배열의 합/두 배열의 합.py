import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
asum = [0]*(n+1)
a = list(map(int, input().split()))
for i in range(n):
    asum[i+1] = asum[i] + a[i]
m = int(input())
bsum = [0]*(m+1)
b = list(map(int, input().split()))
for i in range(m):
    bsum[i+1] = bsum[i] + b[i]

da = dict()
db = dict()
for i in range(n):
    for j in range(i+1, n+1):
        x = asum[j] - asum[i]
        if x in da:
            da[x] += 1
        else:
            da[x] = 1
for i in range(m):
    for j in range(i+1, m+1):
        x = bsum[j] - bsum[i]
        if x in db:
            db[x] += 1
        else:
            db[x] = 1

ans = 0
for x in da:
    y = t - x
    if y in db:
        ans += da[x] * db[y]

print(ans)