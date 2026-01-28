import sys
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

ans = 0
tmp = -float('inf')
for x, y in lines:
    if x > tmp:
        ans += y - x
        tmp = y
    elif y > tmp:
        ans += y - tmp
        tmp = y

print(ans)