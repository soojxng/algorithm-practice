import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = [a[0]]
pos = [0]*n

for i in range(1, n):
    x = bisect.bisect_left(lis, a[i])
    pos[i] = x
    if x >= len(lis):
        lis.append(a[i])
    else:
        lis[x] = a[i]

print(len(lis))
x = len(lis) - 1
ans = []
for i in range(n-1, -1, -1):
    if x < 0:
        break
    if pos[i] == x:
        ans.append(a[i])
        x -= 1
print(*reversed(ans))