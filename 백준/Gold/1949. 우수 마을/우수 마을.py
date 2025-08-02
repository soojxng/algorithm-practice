import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    for v in tree[x]:
        if visited[v] == 0:
            dfs(v)
            dp[x][0] += max(dp[v][0], dp[v][1])
            dp[x][1] += dp[v][0]

n = int(input())
town = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    
dp = [[0, t] for t in town]
visited = [0]*n

dfs(0)
print(max(dp[0]))