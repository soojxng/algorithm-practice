import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    l = max(blocks[:i])
    r = max(blocks[i+1:])
    if l > blocks[i] and r > blocks[i]:
        ans += min(l, r) - blocks[i]

print(ans)