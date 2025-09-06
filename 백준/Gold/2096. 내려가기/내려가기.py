import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

xdp = [0]*3
ndp = [0]*3

n = int(input())
for i in range(n):
    floor = list(map(int, input().split()))
    maxdp = xdp[::]
    mindp = ndp[::]
    for j in range(3):
        xdp[j] = floor[j] + max(maxdp[0] if j != 2 else -1, maxdp[1], maxdp[2] if j != 0 else -1)
        ndp[j] = floor[j] + min(mindp[0] if j != 2 else float('inf'), mindp[1], mindp[2] if j != 0 else float('inf'))

print(max(xdp), min(ndp))