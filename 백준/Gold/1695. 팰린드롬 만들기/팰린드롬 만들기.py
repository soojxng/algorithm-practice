import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    tmp = dp[::]
    for j in range(1, n+1):
        if arr[i-1] == arr[n-j]:
            dp[j] = tmp[j-1] + 1
        else:
            dp[j] = max(dp[j], dp[j-1])

print(n - dp[n])