import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
a = list(map(int, input().split()))

pref = [0]*(m+1)
suff = set()
tot = sum(a)
suff.add(tot)
for i in range(m):
    pref[i+1] = pref[i] + a[i]
    suff.add(tot-pref[i+1])

for _ in range(n):
    q = int(input())
    f = 0
    if q <= tot:
        for p in pref:
            if p > q:
                break
            if q - p in suff:
                f = 1
                break
    print("Yes" if f else "No")