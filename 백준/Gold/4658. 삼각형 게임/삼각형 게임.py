import sys
input = sys.stdin.readline

def bt(s):
    if len(h) == 7:
        if h[0] == h[-1]:
            global ans
            ans = max(ans, s)
        return
    for n in range(1, 6):
        if n in v:
            continue
        v.add(n)
        for i in range(3):
            if h[-1] == t[n][i]:
                h.append(t[n][i-1])
                bt(s+t[n][i-2])
                h.pop()
        v.remove(n)

while 1:
    t = [list(map(int, input().split())) for _ in range(6)]
    h = []
    v = set([0])
    ans = 0
    for i in range(3):
        h = [t[0][i], t[0][i-1]]
        bt(t[0][i-2])
    print(ans if ans else 'none')
    if input().rstrip() == '$':
        break