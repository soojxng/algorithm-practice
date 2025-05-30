import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

s, e = 1, N*N
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = sum(min(mid // i, N) for i in range(1, N+1))
    if cnt < k: s = mid + 1
    else:
        ans = mid
        e = mid - 1
print(ans)