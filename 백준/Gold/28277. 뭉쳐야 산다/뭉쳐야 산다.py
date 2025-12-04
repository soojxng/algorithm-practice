import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = [set() for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    s[i] = set(tmp[1:])

for _ in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        a, b = tmp[1], tmp[2]
        if len(s[a]) < len(s[b]):
            s[a], s[b] = s[b], s[a]
        for x in s[b]:
            s[a].add(x)
        s[b] = set()

    elif tmp[0] == 2:
        print(len(s[tmp[1]]))