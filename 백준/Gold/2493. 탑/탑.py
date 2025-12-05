import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
ans = [0]*n
s = []

for i in range(n):
    while s and tower[s[-1]] < tower[i]:
        s.pop()
    if s:
        ans[i] = s[-1]+1
    s.append(i)

print(*ans)