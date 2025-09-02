import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1, n+1):
    t, s = map(int, input().split())
    arr.append((t, s, i))
arr.sort(key=lambda x: (-x[1]/x[0], x[2]))

for t, s, i in arr:
    print(i, end=' ')