import sys
input = sys.stdin.readline

n, q = map(int, input().split())
li = [0, [0]*(n+1), [0]*(n+1)]
se = [0, set(), set()]
length = [0, [n, 0], [n, 0]]
for _ in range(q):
    t, a = map(int, input().split())
    li[t][a] += 1
    if not se[t]:
        se[t].add(a)
        length[t][0] = 1
        length[t][1] += 1
    elif a in se[t]:
        se[t] = set([a])
        length[t][0] = 1
        length[t][1] += 1
    elif length[t][1] == li[t][a]:
        se[t].add(a)
        length[t][0] += 1

    print(length[1][0]*length[2][0])