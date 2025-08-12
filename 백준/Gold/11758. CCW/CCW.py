import sys
input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(3)]

ans = 0
for i in range(3):
    ans += p[i-1][0]*p[i][1]
for i in range(3):
    ans -= p[i][0]*p[i-1][1]

if ans == 0:
    print(0)
elif ans > 0:
    print(1)
else:
    print(-1)