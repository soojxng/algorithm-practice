import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return 1
    arr[pb] = pa
    return 0

n, m = map(int, input().split())
arr = [i for i in range(n)]
cnt = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    if union(a, b):
        cnt = i
        break
print(cnt)
            