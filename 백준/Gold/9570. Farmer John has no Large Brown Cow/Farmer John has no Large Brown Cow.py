import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [set() for _ in range(30)]
missing = set()

for _ in range(n):
    tmp = list(input().rstrip().split())
    missing.add(tuple(tmp[4:-1]))
    for i in range(4, len(tmp)-1):
        s[i-4].add(tmp[i])

m = len(tmp) - 5
li = [sorted(list(s[i])) for i in range(m)]
pref = []
tot = 1

for i in range(m):
    tot *= len(li[i])

for i in range(m):
    tot //= len(li[i])
    for w in li[i]:
        cnt = tot
        pref.append(w)

        for x in missing:
            if x[:i+1] == tuple(pref):
                cnt -= 1

        if cnt < k:
            k -= cnt
            pref.pop()
        else:
            break

print(*pref)