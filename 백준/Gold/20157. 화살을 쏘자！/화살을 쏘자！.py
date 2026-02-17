import sys
import math
input = sys.stdin.readline

n = int(input())
max_val = 0
d = dict()

for _ in range(n):
    x, y = map(int, input().split())
    z = math.gcd(x, y)
    key = (x//z, y//z)
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    max_val = max(max_val, d[key])
print(max_val)