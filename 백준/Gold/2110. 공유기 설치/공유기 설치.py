import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = sorted([int(input()) for _ in range(N)])
s = 1
e = X[-1] - X[0]
ans = 0

while s <= e:
    mid = (e+s)//2
    cnt = 1
    i = 1
    tmp = 0
    while cnt < C and i < N:
        if tmp + X[i] - X[i-1] >= mid:
            tmp = 0
            cnt += 1
        else:
            tmp += X[i] - X[i-1]
        i += 1
    if cnt < C:
        e = mid-1
    else:
        ans = mid
        s = mid+1
        
print(ans)