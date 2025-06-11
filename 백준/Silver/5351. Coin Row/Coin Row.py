import sys
input = sys.stdin.readline

for _ in range(int(input())):
    C = list(map(int, input().split()))
    dp = [0]*len(C)
    if len(C) <= 2:
        print(max(C))
        continue
    dp[0] = C[0]
    dp[1] = C[1]
    dp[2] = C[0] + C[2]
    for i in range(3, len(C)):
        dp[i] = C[i] + max(dp[i-2], dp[i-3])
    print(max(dp[-1], dp[-2]))