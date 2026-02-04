import sys
input = sys.stdin.readline

n = int(input())
ans = 0
s = []
for _ in range(n):
    h = int(input())
    while s and s[-1] <= h:
        s.pop()
    ans += len(s)
    s.append(h)
print(ans)