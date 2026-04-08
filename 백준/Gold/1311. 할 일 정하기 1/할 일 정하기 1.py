import sys
input = sys.stdin.readline

def cal(visited):
    if visited == (1 << n) - 1:
        return 0
    if dp[visited] < float('inf'):
        return dp[visited]
    
    i = visited.bit_count()

    for j in range(n):
        if visited & (1 << j):
            continue
        dp[visited] = min(dp[visited], cal(visited | (1 << j)) + d[i][j])
        
    return dp[visited]

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
dp = [float('inf')]*(1 << n)
print(cal(0))