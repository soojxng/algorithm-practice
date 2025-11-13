import sys
input = sys.stdin.readline

def dfs(v):
    cnt = 0
    if not tree[v]:
        return 1
    for u in tree[v]:
        cnt += dfs(u)

    return cnt

n = int(input())
parents = list(map(int, input().split()))
x = int(input())
parents[x] = x

tree = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

print(dfs(root) if root != -1 else 0)