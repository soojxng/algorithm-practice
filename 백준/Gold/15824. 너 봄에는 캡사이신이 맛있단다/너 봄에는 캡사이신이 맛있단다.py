import sys
input = sys.stdin.readline

MOD = 1000000007
n = int(input())
scv = list(map(int, input().split()))
scv.sort()

sq2 = [1]
for i in range(1, n):
    sq2.append(sq2[i-1] * 2 % MOD)

ans = 0
for i in range(n):
    ans = (ans + scv[i] * (sq2[i] - sq2[n-1-i])) % MOD
print(ans)