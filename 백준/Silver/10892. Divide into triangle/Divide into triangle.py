import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(1, N*3+1):
    x, y = map(int, input().split())
    arr.append((x, y, i))
arr = sorted(arr)
for i in range(len(arr)):
    print(arr[i][2], end=' ')
    if (i+1) % 3 == 0:
        print()