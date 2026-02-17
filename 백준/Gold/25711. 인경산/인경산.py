import sys
import math
input = sys.stdin.readline

n, q = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
dist = [0]*n
dist_asc = [0]*n
dist_desc = [0]*n

for k in range(1, n):
    dist[k] = math.sqrt((x[k]-x[k-1])**2 + (y[k]-y[k-1])**2)
for k in range(1, n):
    w = 1 if y[k] < y[k-1] else (2 if y[k] == y[k-1] else 3)
    dist_asc[k] = dist_asc[k-1] + (dist[k]*w)
for k in range(n-2, -1, -1):
    w = 1 if y[k] < y[k+1] else (2 if y[k] == y[k+1] else 3)
    dist_desc[k] = dist_desc[k+1] + (dist[k+1]*w)

for _ in range(q):
    i, j = map(int, input().split())
    ans = (dist_asc[j-1] - dist_asc[i-1]) if i < j else (dist_desc[j-1] - dist_desc[i-1])
    print(ans)