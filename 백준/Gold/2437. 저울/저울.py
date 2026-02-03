import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
weights.sort()

ans = 1
for w in weights:
    if ans < w:
        break
    ans += w

print(ans)