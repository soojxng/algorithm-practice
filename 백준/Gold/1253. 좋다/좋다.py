import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = 0
for i in range(n):
    l = 0
    r = n-1
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        x = a[l] + a[r]
        if a[i] < x:
            r -= 1
        elif a[i] > x:
            l += 1
        else:
            cnt += 1
            break

print(cnt)