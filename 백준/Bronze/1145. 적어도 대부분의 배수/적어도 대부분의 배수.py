S = sorted(list(map(int, input().split())))
n = S[2]
while 1:
    cnt = 0
    for s in S:
        if n % s == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1