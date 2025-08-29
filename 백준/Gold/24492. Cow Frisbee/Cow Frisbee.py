import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
s = []
ans = 0
for i in range(n):
    while s and h[s[-1]] < h[i]:
        ans += i-s[-1]+1
        s.pop()
    if s:
        ans += i-s[-1]+1
    s.append(i)
print(ans)