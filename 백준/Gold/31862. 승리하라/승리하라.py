import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
scores = [0]*(n+1)
games = []
for _ in range(m):
    t1, t2, f = map(int, input().split())
    if f == 1:
        scores[t1] += 1
    elif f == 2:
        scores[t2] += 1
    else:
        games.append((t1, t2))

max_val = max(scores)
cnt = scores.count(max_val)
length = len(games)
ans = 0

for b in range(1 << length):
    tmp = dict()
    tmp[k] = 0
    nmax = max_val
    ncnt = cnt

    for i in range(length):
        x, y = games[i]
        z = 0
        if (b >> i) & 1:
            z = x
        else:
            z = y
        
        if z in tmp:
            tmp[z] += 1
        else:
            tmp[z] = 1

        if scores[z] + tmp[z] == nmax:
            ncnt += 1
        elif scores[z] + tmp[z] > nmax:
            nmax = scores[z] + tmp[z]
            ncnt = 1

    if ncnt == 1 and scores[k] + tmp[k] == nmax:
        ans += 1

print(ans)