import sys
input = sys.stdin.readline

r, c = map(int, input().split())
ard = set()
js = []

for i in range(r):
    tmp = input().rstrip()
    for j in range(c):
        if tmp[j] == 'R':
            ard.add((i, j))
        elif tmp[j] == 'I':
            js = (i, j)

d = ((0, 0), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1))
move = list(map(int, list(input().rstrip())))

f = 0
for x in range(len(move)):
    dx, dy = d[move[x]]
    js = (js[0]+dx, js[1]+dy)
    if js in ard:
        f = x+1
        break
    ard_nxt = set()
    tmp = set()
    for a, b in ard:
        if a < js[0]:
            a += 1
        elif a > js[0]:
            a -= 1
        if b < js[1]:
            b += 1
        elif b > js[1]:
            b -= 1

        if (a, b) == js:
            f = x+1
            break

        if (a, b) not in ard_nxt:
            ard_nxt.add((a, b))
        else:
            tmp.add((a, b))

    if f:
        break
    ard = ard_nxt - tmp

if f:
    print('kraj', f)
else:
    ans = [['.']*c for _ in range(r)]
    for a, b in ard:
        ans[a][b] = 'R'
    ans[js[0]][js[1]] = 'I'

    for a in ans:
        print(''.join(a))

