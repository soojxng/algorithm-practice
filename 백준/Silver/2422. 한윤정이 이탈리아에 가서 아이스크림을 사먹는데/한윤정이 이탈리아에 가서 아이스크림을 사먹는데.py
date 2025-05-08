import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = set()
for _ in range(M):
    a, b = map(int, input().split())
    arr1.add((a, b) if a < b else (b, a))

cnt = 0
for i in combinations(range(1, N+1), 3):
    if (i[0], i[1]) in arr1 or (i[0], i[2]) in arr1 or (i[1], i[2]) in arr1:
        continue
    cnt += 1

print(cnt)