import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    P = list(map(float, input().split()))
    dp = [0]*n
    if n <= 3:
        print(round(max(P), 2))
        continue
    dp[0] = P[0]
    dp[1] = P[1]
    dp[2] = P[2]
    dp[3] = P[0] + P[3]
    if n == 4:
        print(round(max(dp), 1))
        continue
    dp[4] = P[4] + max(dp[0], dp[1])
    if n == 5:
        print(round(max(dp), 1))
        continue
    for i in range(5, n):
        dp[i] = P[i] + max(dp[i-3], dp[i-4], dp[i-5])
    print(round(max(dp[-1], dp[-2], dp[-3]), 1))