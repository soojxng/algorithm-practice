import sys
input = sys.stdin.readline

K, N = map(int, input().split())

LAN = [int(input()) for _ in range(K)]

l, r = 1, max(LAN)
ans = 0

while l <= r:
    mid = (l + r) // 2
    cnt = sum(i // mid for i in LAN)

    if cnt < N:
        r = mid - 1
    else:
        ans = mid
        l = mid + 1

print(ans)
