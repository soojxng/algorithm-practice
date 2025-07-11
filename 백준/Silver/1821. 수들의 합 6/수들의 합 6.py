import sys
from itertools import permutations
input = sys.stdin.readline

N, F = map(int, input().split())
l = [x for x in range(1, N+1)]
P = permutations(l, N)
f = 0
for p in P:
    tmp = list(p)
    while len(p) > 1:
        p = [p[i] + p[i+1] for i in range(len(p)-1)]
    if p[0] == F:
        print(*tmp)
        break