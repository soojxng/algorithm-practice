import sys
input = sys.stdin.readline

n = int(input())
inc = []
dec = []
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        inc.append((a, b))
    else:
        dec.append((a, b))

inc.sort()
dec.sort(key=lambda x: x[1], reverse=1)

ans = 0
tmp = 0
for a, b in inc + dec:
    if tmp < a:
        x = a - tmp
        ans += x
        tmp = b
    else:
        tmp += b - a

print(ans)