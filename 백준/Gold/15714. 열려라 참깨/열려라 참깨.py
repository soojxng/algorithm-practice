import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(n):
    z = y[i] - x[i]
    ans += abs(z - tmp)
    tmp = z

ans += abs(0-tmp)
print(ans // 2)