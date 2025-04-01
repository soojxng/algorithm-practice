import sys
input = sys.stdin.readline

S = set()
allS = set(range(1, 21))

for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'add':
        S.add(int(tmp[1]))
    elif tmp[0] == 'remove':
        S.discard(int(tmp[1])) 
    elif tmp[0] == 'check':
        print(1 if int(tmp[1]) in S else 0)
    elif tmp[0] == 'toggle':
        S.discard(int(tmp[1])) if int(tmp[1]) in S else S.add(int(tmp[1]))
    elif tmp[0] == 'all':
        S = allS.copy()
    elif tmp[0] == 'empty':
        S.clear()
        