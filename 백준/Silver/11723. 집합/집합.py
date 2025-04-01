import sys
input = sys.stdin.readline

emptyS = [0 for _ in range(21)]
allS = [1 for _ in range(21)]
S = emptyS[:]

for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'add':
        S[int(tmp[1])] = 1
    elif tmp[0] == 'remove':
        S[int(tmp[1])] = 0
    elif tmp[0] == 'check':
        print(S[int(tmp[1])])
    elif tmp[0] == 'toggle':
        S[int(tmp[1])] = 0 if S[int(tmp[1])] else 1
    elif tmp[0] == 'all':
        S = allS[:]
    elif tmp[0] == 'empty':
        S = emptyS[:]
        