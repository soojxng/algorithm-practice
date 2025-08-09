import sys
input = sys.stdin.readline
        
n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [[0]*n for _ in range(n)]
for j in range(n):
    for i in range(n):
        if i+j >= n:
            break
        if j == 0:
            dp[i][i+j] = 1
        elif j == 1 and a[i] == a[i+j]:
            dp[i][i+j] = 1
        elif dp[i+1][i+j-1] == 1 and a[i] == a[i+j]:
            dp[i][i+j] = 1
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])