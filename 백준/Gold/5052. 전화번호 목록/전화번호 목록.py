import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    tel = [input().rstrip() for _ in range(n)]
    tel.sort()
    s = set([tel[0]])
    f = True
    for i in range(1, n):
        tmp = ''
        for j in range(len(tel[i])-1):
            tmp += tel[i][j]
            if tmp in s:
                f = False
                print('NO')
                break
        if f:
            s.add(tel[i])
        else:
            break

    if f:
        print('YES')