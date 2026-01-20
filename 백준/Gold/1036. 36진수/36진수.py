import sys
input = sys.stdin.readline
    
d = dict()
for i in range(0, 10):
    d[str(i)] = i
for i in range(10, 36):
    d[chr(i+55)] = i

n = int(input())
tot = 0
a = [0]*36
for _ in range(n):
    s = input().rstrip()
    x = 36**(len(s)-1)

    for i in range(len(s)):
        tot += d[s[i]] * x
        a[d[s[i]]] += (35 - d[s[i]]) * x
        x //= 36

k = int(input())
a.sort(reverse=1)
tot += sum(a[:k])

if tot == 0:
    print(0)
else:
    tmp = sorted(list(d.keys()))
    result = []
    while tot > 0:
        result.append(tmp[tot % 36])
        tot //= 36
    print(''.join(result[::-1]))