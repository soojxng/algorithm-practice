import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    impq = deque([i, imp[i]] for i in range(N))
    imp.sort(reverse=1)
    i = 0
    
    while 1:
        if impq[0][1] == imp[i]:
            tmp = impq.popleft()[0]
            if tmp == M:
                print(i + 1)
                break
            i += 1
        else:
            impq.rotate(-1)