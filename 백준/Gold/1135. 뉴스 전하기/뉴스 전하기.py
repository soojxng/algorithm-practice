import sys
input = sys.stdin.readline

def dfs(v):
    tmp = []
    for u in tree[v]:
        dfs(u)
        tmp.append(dp[u])
    
    tmp.sort(reverse=1)
    for i in range(len(tmp)):
        dp[v] = max(dp[v], tmp[i] + i + 1)

n = int(input())
parents = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[parents[i]].append(i)

dp = [0]*n
dfs(0)
print(dp[0])