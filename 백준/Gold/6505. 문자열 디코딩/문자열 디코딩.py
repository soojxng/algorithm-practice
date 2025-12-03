import sys
input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    p = list(map(lambda x: x-1, map(int, input().split())))
    s = input().rstrip('\n')

    visited = [0]*n
    cycle = []
    for i in range(n):
        if not visited[i]:
            tmp = []
            x = i
            while not visited[x]:
                visited[x] = 1
                tmp.append(x)
                x = p[x]
            cycle.append(tmp)

    ans = [0]*n
    for c in cycle:
        size = len(c)
        for i in range(size):
            ans[c[(i+m) % size]] = s[c[i]]

    print(''.join(ans))