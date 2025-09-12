import sys
input = sys.stdin.readline

n = int(input())
joker = 0
a = [list(map(int, input().split())) for _ in range(n)]

for aa in a:
    f = 1
    cnt = 0
    tmp = [0, 13]
    for j in range(len(aa)):
        if f == -1:
            break
        if tmp[f] <= joker < tmp[f] + aa[j]:
            joker = cnt + joker - tmp[f]
            f = -1
        else:
            tmp[f] += aa[j]
            cnt += aa[j]
            f = 0 if f else 1

print(joker+1)