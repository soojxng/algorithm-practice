import sys
input = sys.stdin.readline

def find(v):
    while parents[v] != v:
        v = parents[v]
    return v

n, q = map(int, input().split())

parents = [i for i in range(n+1)]
for i in range(2, n+1):
    a = int(input())
    parents[i] = a

for _ in range(n - 1 + q):
    tmp = list(map(int, input().split()))
    if not tmp[0]:
        parents[tmp[1]] = tmp[1]
    else:
        print('YES' if find(tmp[1]) == find(tmp[2]) else 'NO')