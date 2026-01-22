import sys
input = sys.stdin.readline

t = int(input())
cases = [int(input()) for _ in range(t)]
n = max(cases)
f = [1]*(n+1)
f[0] = 0
g = [0]*(n+1)

for i in range(2, n+1):
    for j in range(i, n+1, i):
        f[j] += i
for i in range(1, n+1):
    g[i] = g[i-1] + f[i]

for x in cases:
    print(g[x])