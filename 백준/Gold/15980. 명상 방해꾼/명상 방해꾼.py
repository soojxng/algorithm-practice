import sys
input = sys.stdin.readline

n, m = map(int, input().split())
singing = [0] * n
pref = [0]*(m+1)
ans = [float('inf'), -1]

for i in range(n):
    d, tmp = input().rstrip().split()
    if d == 'L':
        singing[i] = list(map(lambda x: -int(x), list(tmp)))
    elif d == 'R':
        singing[i] = list(map(int, list(tmp)))
    for j in range(m):
        pref[j+1] += singing[i][j]

for j in range(1, m+1):
    pref[j] += pref[j-1]

for i in range(n):
    tot = 0
    tmp = 0
    for j in range(m):
        tot += singing[i][j]
        tmp = max(tmp, abs(pref[j+1] - tot))
    if tmp < ans[0]:
        ans = [tmp, i]
    if ans[0] == 0:
        break

print(ans[1]+1)
print(ans[0])