import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]

n, m = map(int, input().split())
arr = [i for i in range(0, n+1)]
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        pa = find(a)
        pb = find(b)
        if pa != pb:
            arr[pb] = pa
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')     