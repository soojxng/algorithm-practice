import sys
input = sys.stdin.readline

n, k = map(int, input().split())

s = list(map(int, input().split()))
d = list(map(lambda x: x-1, map(int, input().split())))

visited = [0]*n
cycle = []
for i in range(n):
    if not visited[i]:
        tmp = []
        x = i
        while not visited[x]:
            visited[x] = 1
            tmp.append(x)
            x = d[x]
        cycle.append(tmp)

ans = [0]*n
for c in cycle:
    size = len(c)
    for i in range(size):
        ans[c[(i+k) % size]] = s[c[i]]

print(*ans)