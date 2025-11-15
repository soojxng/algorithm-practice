import sys
input = sys.stdin.readline

n = int(input())
goat = list(map(int, input().split()))
coords = [[i, 0] for i in range(n)]
for i in range(4):
    coords[goat[i]-1][1] = -1 if i < 2 else 1
coords[0][0] = -1000000
coords[n-1] = [1000000, 1000000 if coords[n-1][1] != -1 else -1000000]

for x, y in coords:
    print(x, y)