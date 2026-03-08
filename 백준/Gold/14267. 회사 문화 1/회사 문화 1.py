import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    for u in tree[v]:
        dp[u] += dp[v]
        dfs(u)

n, m = map(int, input().split())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[parents[i]-1].append(i)

dp = [0]*n
for _ in range(m):
    i, w = map(int, input().split())
    dp[i-1] += w
dfs(0)
print(*dp)