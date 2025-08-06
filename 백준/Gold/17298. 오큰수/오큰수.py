s = [(-1, float('inf'))]
n = int(input())
a = list(map(int, input().split()))
ans = [-1] * n
for i in range(n):
    while s[-1][1] < a[i]:
        j, b = s.pop()
        ans[j] = a[i]
    s.append((i, a[i]))
print(*ans)