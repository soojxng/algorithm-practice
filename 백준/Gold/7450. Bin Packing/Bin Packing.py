import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
arr = sorted(list(int(input()) for _ in range(n)))
i = 0
cnt = 0
for j in range(n-1, -1, -1):
    if i == j:
        cnt += 1
        break
    if j < i:
        break
    if arr[i] + arr[j] <= l:
        i += 1
    cnt += 1
print(cnt)