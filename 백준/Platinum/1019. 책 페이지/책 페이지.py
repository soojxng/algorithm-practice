import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*10

tmp = 1
for _ in range(len(str(n))):
    h = n // (tmp*10)
    x = (n//tmp) % 10
    l = n % tmp
    ans[0] -= tmp

    for i in range(10):
        ans[i] += h*tmp + (tmp if i < x else 0)
    ans[x] += l+1

    tmp *= 10

print(*ans)