import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]

n = int(input())
m = int(input())
arr = [i for i in range(0, n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i+1, n):
        if tmp[j] == 1:
            pi = find(i)
            pj = find(j)
            if pi != pj:
                arr[pj] = pi
plan = [find(x-1) for x in map(int, input().split())]
for i in range(m-1):
    if plan[i] != plan[i+1]:
        print('NO')
        break
else:
    print('YES')