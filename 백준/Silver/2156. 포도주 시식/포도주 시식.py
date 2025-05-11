import sys
input = sys.stdin.readline

n = int(input())
grapes = [int(input()) for _ in range(n)]
arr = [0]*n
arr[0] = grapes[0]
if n > 1:
    arr[1] = grapes[0] + grapes[1]
if n > 2:
    arr[2] = max(grapes[0] + grapes[2], grapes[1] + grapes[2], arr[1])
for i in range(3, n):
    arr[i] = max(arr[i-1], arr[i-2] + grapes[i], arr[i-3] + grapes[i-1] + grapes[i])
print(arr[-1])
