n = int(input())

li = list(map(int, input().split()))
s = list(set(li))
s.sort()
d = {s[i]:i for i in range(len(s))}
for i in li:
    print(d[i], end=' ')