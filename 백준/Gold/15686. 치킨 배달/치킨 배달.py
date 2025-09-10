import sys
input = sys.stdin.readline

def bt(start):
    if len(com) == m:
        cnt[0] = min(
            cnt[0],
            sum(min(abs(hx-chicken[i][0])+abs(hy-chicken[i][1]) for i in com) for hx, hy in houses)
            )
        return

    for i in range(start, len(chicken)):
        com.append(i)
        bt(i+1)
        com.pop()

n, m = map(int, input().split())
houses = []
chicken = []
com = []
cnt = [float('inf')]

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j] == 1:
            houses.append((i, j))
        elif s[j] == 2:
            chicken.append((i, j))

bt(0)
print(cnt[0])