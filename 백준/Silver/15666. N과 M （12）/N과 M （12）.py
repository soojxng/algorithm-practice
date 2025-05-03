import sys
input = sys.stdin.readline

def combination_rep(start):
    if len(tmp) == M:
        s.add(tuple(tmp))
        return
    
    for i in range(start, len(l)):
        tmp.append(l[i])
        combination_rep(i)
        tmp.pop()

N, M = map(int, input().split())
l = list(set(map(int, input().split())))
l.sort()
tmp = []
s = set()       
combination_rep(0)
for i in sorted(s):
    print(' '.join(map(str, i)))