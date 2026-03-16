import sys
input = sys.stdin.readline

def cal(v, visited):
    if dp[v][visited] is not None:
        return dp[v][visited]
    if visited == (1 << n) - 1:
        return w[v][0] if w[v][0] else float('inf')
    
    tmp = float('inf')
    for u in range(n):
        if w[v][u] == 0 or visited & (1 << u):
            continue
        tmp = min(tmp, cal(u, visited | (1 << u)) + w[v][u])
    dp[v][visited] = tmp
    return dp[v][visited]

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[None]*(1 << n) for _ in range(n)]
print(cal(0, 1))