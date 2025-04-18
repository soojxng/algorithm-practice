import sys
input = sys.stdin.readline

N, K = map(int, input().split())
v = [0 for _ in range(K*2+1 if K > N else N*2+1)]

tmp = set()
tmp.add(N)
cnt = 0

while tmp:
    tmp2, tmp= tmp, set()
    if K in tmp2:
        print(cnt)
        break
    cnt += 1
    for i in tmp2:
        v[i] = 1 
        for j in [i-1, i+1, i*2]:
            if 0 <= j < len(v) and not v[j]:
                tmp.add(j)