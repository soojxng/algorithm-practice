import sys
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth = set(truth[1:])
parent = [i if i not in truth else 0 for i in range(n+1)]
party = []
for i in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
    minimum = float('inf')
    for j in range(1, tmp[0]+1):
        minimum = min(minimum, find(tmp[j]))
    for j in range(1, tmp[0]+1):
        pj = find(tmp[j])
        parent[pj] = minimum

cnt = 0
for i in range(m):
    f = 1
    for p in party[i]:
        if find(p) == 0:
            f = 0
            break
    cnt += f

print(cnt)