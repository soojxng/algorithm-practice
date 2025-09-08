import sys
input = sys.stdin.readline

t = int(input())
#d[pid] = [실행시간, 우선순위] 
d = dict()
pids = list(map(int, input().split()))

prev = None
tmp = t
for i in range(t-1, -1, -1):
    x = pids[i]
    if prev and prev > x:
        tmp -= 1
    if x not in d:
        d[x] = [1, tmp - i]
    else:
        d[x][0] += 1
        d[x][1] = tmp - i
    prev = x

print(len(d))
for key in sorted(d.keys()):
    print(key, d[key][0], d[key][1])