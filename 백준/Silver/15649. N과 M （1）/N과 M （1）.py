import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
l = [x for x in range(1, N+1)]
P = permutations(l, M)

for p in P:
    print(' '.join(map(str, p)))