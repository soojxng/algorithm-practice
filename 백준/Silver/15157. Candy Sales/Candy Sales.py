import sys
input = sys.stdin.readline

n = int(input())
min_val = float('inf')
ans = []
for c in map(int, input().split()):
    min_val = min(c, min_val)
    ans.append(str(min_val))
    min_val += 1
print(' '.join(ans))