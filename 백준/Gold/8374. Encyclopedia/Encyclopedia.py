import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(2*n)]

ans = [0, 0]
cnt = 0

i = 0
while cnt < n:
    if arr[i] == 0:
        ans[0] += abs(i-(cnt*2))
        ans[1] += abs(i-(cnt*2+1))
        cnt += 1
    i += 1

print(min(ans))