import sys
input = sys.stdin.readline

def cal(v):
    if not tree[v]:
        return 2
    tmp = 1
    for vv in tree[v]:
        tmp *= cal(vv)
    return tmp + 1

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(1, n):
    x = int(input())
    tree[x].append(i)

ans = 1
for v in tree[n]:
    ans *= cal(v)

print(ans)