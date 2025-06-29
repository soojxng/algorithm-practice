import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0]*N for _ in range(N)]
    f = N % 2
    
    for l in range(N):
        for i in range(N-l):
            if l == 0:
                dp[i][i+l] = cards[i] if f else 0
            elif f:
                dp[i][i+l] = max(dp[i+1][i+l]+cards[i], dp[i][i+l-1]+cards[i+l])
            else:
                dp[i][i+l] = min(dp[i+1][i+l], dp[i][i+l-1])
        f = 0 if f else 1
    print(dp[0][N-1])
    