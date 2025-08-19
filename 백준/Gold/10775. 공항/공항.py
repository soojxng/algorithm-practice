import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]

def union(a):
    pa = find(a)
    if pa == 0:
        return 0
    arr[pa] = find(pa-1)
    return 1

g = int(input())
p = int(input())
arr = list(range(g+1))
tmp = [int(input()) for _ in range(p)]
cnt = 0
for x in tmp:
    if not union(x):
        break
    cnt += 1
print(cnt)