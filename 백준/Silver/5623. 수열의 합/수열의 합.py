import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
if n == 2:
    print(1, 1)
else:
    tmp = (arr[0][1] + arr[0][2] - arr[1][2]) // 2
    print(tmp, end=' ')
    print(' '.join(map(str, (arr[i][0] - tmp for i in range(1, n)))))