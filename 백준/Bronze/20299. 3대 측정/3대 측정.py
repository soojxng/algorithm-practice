import sys
input = sys.stdin.readline

ans = []
n, k, l = map(int, input().split())
for _ in range(n):
    x = list(map(int, input().split()))
    if min(x) >= l and sum(x) >= k:
        ans += x
print(len(ans)//3)
print(*ans)
