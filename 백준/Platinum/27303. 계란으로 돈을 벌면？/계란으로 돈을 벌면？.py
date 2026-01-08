import sys
input = sys.stdin.readline

k = int(input())
MOD = 1000000007
k2 = k % (MOD-1)
ans = (k + 1) * (pow(2, k % (MOD-1), MOD) - 1) - (k * pow(2, (k-1) % (MOD-1), MOD))
ans %= MOD
print(ans)