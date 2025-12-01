import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
b = set()
if m > 0:
    b = set(input().rstrip().split())

ans = abs(n-100)
for i in range(1000001):
    num = str(i)
    for c in num:
        if c in b:
            break
    else:
        ans = min(ans, len(num) + (abs(n-i)))

print(ans)