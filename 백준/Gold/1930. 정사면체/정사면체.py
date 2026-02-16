import sys
input = sys.stdin.readline

side = ((1, 2, 3), (0, 3, 2), (3, 0, 1), (2, 1, 0))  
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    a = tmp[:4]
    b = tmp[4:]
    f = 0
    for i in range(4):
        if f:
            break
        if b[i] == a[0]:
            tmp = []
            for j in side[i]:
                tmp.append(b[j])

            for i in range(3):
                if a[1] == tmp[0-i] and a[2] == tmp[1-i] and a[3] == tmp[2-i]:
                    f = 1
                    break
    print(f)