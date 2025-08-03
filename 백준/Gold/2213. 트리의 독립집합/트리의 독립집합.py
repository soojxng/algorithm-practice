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
            
def trace(x, f):
    visited[x] = 0
    if f or dp[x][0] > dp[x][1]:
        for v in tree[x]:
            if visited[v] == 1:
                trace(v, 0)
    else:
        arr.append(x)
        for v in tree[x]:
            if visited[v] == 1:
                trace(v, 1)
    
n = int(input())
volume = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
dp = [[0, 0]] + [[0, v] for v in volume]
visited = [0]*(n+1)

dfs(1)
print(max(dp[1]))

arr = []
trace(1, 0)
arr.sort()
print(*arr)