import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
dp = [[[] for _ in range(len(b)+1)] for _ in range(len(a)+1)]
dp[0][0] = ['']

for j in range(len(a)+1):
    for k in range(len(b)+1):
        if j > 0 and dp[j-1][k] and a[j-1] == c[j+k-1]:
            dp[j][k] = dp[j-1][k][:] + ['1']
        if k > 0 and dp[j][k-1] and b[k-1] == c[j+k-1]:
            dp[j][k] = dp[j][k-1][:] + ['2']

print(''.join(dp[-1][-1]))