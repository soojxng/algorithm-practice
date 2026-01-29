import sys
input = sys.stdin.readline

MOD = 10**6
s = input().rstrip()

dp = [0]*(len(s)+1)
dp[0] = 1
if s[0] != '0': dp[1] = 1

tmp = int(s[0])
for i in range(2, len(s)+1):
    if dp[i-1] == 0:
        break
    tmp = (tmp * 10) + int(s[i-1])
    if 10 <= tmp <= 26:
        dp[i] = (dp[i] + dp[i-2]) % MOD
    tmp %= 10
    if tmp > 0:
        dp[i] = (dp[i] + dp[i-1]) % MOD

print(dp[-1]) 
