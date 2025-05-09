import sys
input = sys.stdin.readline

N, M, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(q):
    i = list(map(int, input().split()))
    if i[0] == 0:
        arr[i[1]][i[2]] = i[3]
    elif i[0] == 1:
        arr[i[1]], arr[i[2]] = arr[i[2]], arr[i[1]]
        
for a in arr:
    print(' '.join(map(str, a)))
