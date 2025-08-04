n = int(input())
a = list(input().rstrip())
m = len(a)
for i in range(n):
    for j in range(i, i+m):
        print(a[j%m], end='')