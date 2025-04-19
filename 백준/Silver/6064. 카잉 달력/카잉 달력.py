import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    y = y if y != N else 0
    v = [0 for _ in range(N)]
    i = 0
    while 1:
        tmp = i*M + x
        tmp2 = tmp%N
        if v[tmp2]:
            print(-1)
            break
        elif tmp2 == y:
            print(tmp)
            break
        v[tmp2] = 1
        i += 1