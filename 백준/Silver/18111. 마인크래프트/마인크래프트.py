import sys
from collections import Counter
input = sys.stdin.readline

N, M, B = map(int, input().split())
grounds = []

for _ in range(N):
    grounds += list(map(int, input().split()))

floors = Counter(grounds)
l = min(grounds)
h = max(grounds)
time = float('inf')
ans = -1

for i in range(l, h+1):
    up, down = 0, 0
    for f, n in floors.items():
        if f > i:
            up += (f - i) * n
        elif f < i:
            down += (i - f) * n
    tmp = 2*up + down
    if down <= up + B and tmp <= time:
        time = tmp
        ans = i
        
print(time, ans)