import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
l = list(map(int, input().split()))
P = set(permutations(l, M))

for p in sorted(P):
    print(' '.join(map(str, p)))