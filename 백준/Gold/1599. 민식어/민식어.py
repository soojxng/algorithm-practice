import sys
input = sys.stdin.readline

minsik = ('a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y')
ms = dict()
for i in range(len(minsik)):
    ms[minsik[i]] = i

n = int(input())
li = []
for _ in range(n):
    w = input().rstrip()
    i = 0
    tmp = []
    while i < len(w):
        if w[i] == 'n' and i < len(w)-1 and w[i+1] == 'g':
            tmp.append(ms['ng'])
            i += 2
        else:
            tmp.append(ms[w[i]])
            i += 1
    li.append([tmp, w])

li.sort()
for w in li:
    print(w[1])