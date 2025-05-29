import sys
input = sys.stdin.readline

p = 10**9+7

for i in range(1, int(input())+1):
    C, V, L = map(int, input().split())
    dp = [[0]*2 for _ in range(L+1)]
    dp[0][1] = 1
    for j in range(1, L+1):
        dp[j][0] = (dp[j-1][0]+dp[j-1][1])*V % p
        dp[j][1] = dp[j-1][0]*C % p
    print(f'Case #{i}: {(dp[L][0] + dp[L][1]) % p}')