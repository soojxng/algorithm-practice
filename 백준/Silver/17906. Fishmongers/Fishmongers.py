import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = sorted(list(map(int, input().split())), reverse=1)
arr = []
for _ in range(m):
    x, p = map(int, input().split())
    arr.append([p, x])
i = 0
ans = 0
for p, x in sorted(arr, reverse=1):
    if i >= n: break
    for _ in range(x):
        if i >= n: break
        ans += w[i]*p
        i += 1
print(ans)